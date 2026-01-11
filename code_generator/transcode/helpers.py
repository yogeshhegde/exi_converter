
def get_target_dict(ns_view):
    # Try old attributes first for backwards compatibility
    for attr in ('_target_dict', 'target_dict'):
        if hasattr(ns_view, attr):
            return getattr(ns_view, attr)
    # For new xmlschema 4.x, NamespaceView doesn't have _target_dict
    # Instead, we need to access the underlying map which includes all namespaces
    # The NamespaceView is iterable and returns (name, element) pairs
    if hasattr(ns_view, 'items'):
        # Convert to dict - this includes elements from target namespace and imports
        return dict(ns_view.items())
    raise AttributeError("No known target dict found in NamespaceView")