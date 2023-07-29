
def apply_like_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_like_photo(photo):
    # TODO: fix this when authefication is ready
    photo.is_liked_by_user = photo.likes_count > 0

    return photo
