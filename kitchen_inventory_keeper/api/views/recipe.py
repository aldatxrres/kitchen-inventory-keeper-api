from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models.recipe import RecipeModel
from api.serializers.recipe import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return RecipeModel.objects.all()
        
        return RecipeModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user

        return super().perform_create(serializer)