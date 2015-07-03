def make_superuser(strategy, details, user=None, *args, **kwargs):
    """Update user to superuser so they can login to the admin."""
    if user:
        setattr(user, 'is_staff', True)
        setattr(user, 'is_superuser', True)
        strategy.storage.user.changed(user)