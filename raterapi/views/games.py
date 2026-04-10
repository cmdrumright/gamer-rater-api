from rest_framework import viewsets, status, serializers, permissions
from rest_framework.response import Response
from raterapi.models import Game, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class GameSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True, source="categories"
    )

    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "description",
            "release_year",
            "player_count",
            "completion_hours",
            "recommended_age",
            "categories",
            "category_ids",
            "is_owner",
        ]
        read_only_fields = ["user"]

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.user


class GameViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        games = Game.objects.select_related("user").prefetch_related("categories").all()
        serializer = GameSerializer(games, many=True, context={"request": request})
        return Response(serializer.data)

    def create(self, request):
        try:
            category_ids = request.data.get("categories", [])
            categories = Category.objects.filter(pk__in=category_ids)

            game = Game.objects.create(
                user=request.user,
                title=request.data.get("title"),
                description=request.data.get("description"),
                release_year=request.data.get("release_year"),
                player_count=request.data.get("player_count"),
                completion_hours=request.data.get("completion_hours"),
                recommended_age=request.data.get("recommended_age"),
            )
            game.categories.set(categories)

            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response({"error": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            game = (
                Game.objects.select_related("user")
                .prefetch_related("categories")
                .get(pk=pk)
            )
            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data)

        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)

            if game.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            game.title = request.data.get("title", game.title)
            game.description = request.data.get("description", game.description)
            game.release_year = request.data.get("release_year", game.release_year)
            game.player_count = request.data.get("player_count", game.player_count)
            game.completion_hours = request.data.get(
                "completion_hours", game.completion_hours
            )
            game.recommended_age = request.data.get(
                "recommended_age", game.recommended_age
            )
            game.save()

            category_ids = request.data.get("categories")
            if category_ids is not None:
                game.categories.set(category_ids)

            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data)

        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)

            if game.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
