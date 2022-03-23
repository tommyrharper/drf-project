from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    def get_len_name(self, data):
        return len(data.title)

    # object level validator
    def validate(self, data):
        if data["title"] == data["storyline"]:
            raise serializers.ValidationError("Title and storyline must be different")
        else:
            return data

    # field level validator
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long"
            )
        else:
            return value


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"


# # validator
# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('Name must be at least 3 characters long')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         movie = Movie.objects.create(**validated_data)
#         return movie

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # object level validator
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description must be different')
#         else:
#             return data

#     ## field level validator
#     # def validate_name(self, value):
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError("Name must be at least 3 characters long")
#     #     else:
#     #         return value
