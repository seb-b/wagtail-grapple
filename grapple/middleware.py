import inspect
from functools import partial

from graphene import ResolveInfo
from graphql.execution.middleware import MIDDLEWARE_RESOLVER_FUNCTION

from .registry import registry

ROOT_TYPES = ["Query", "Mutation", "Subscription"]


def get_middleware_resolvers(middlewares):
    for middleware in middlewares:
        if inspect.isfunction(middleware):
            yield middleware
        elif inspect.isclass(middleware):
            if hasattr(middleware, MIDDLEWARE_RESOLVER_FUNCTION):
                yield getattr(middleware(), MIDDLEWARE_RESOLVER_FUNCTION)
            else:
                raise AttributeError(
                    f"Middleware {middleware} must have a {MIDDLEWARE_RESOLVER_FUNCTION} function"
                )
        else:
            raise Exception(
                "Middleware must be either a class or a function. Got: {}.\nYou can read more about middleware here: https://docs.graphene-python.org/en/latest/execution/middleware/".format(
                    type(middleware)
                )
            )


class IsAuthenticatedMiddleware(object):
    def resolve(self, next, root, info, **args):
        if not info.context.user.is_authenticated:
            return None
        return next(root, info, **args)


class IsAnonymousMiddleware(object):
    def resolve(self, next, root, info, **args):
        if not info.context.user.is_anonymous:
            return None
        return next(root, info, **args)


class GrappleMiddleware(object):
    def __init__(self):
        self.field_middlewares = {}
        for field_name in registry.field_middlewares:
            self.field_middlewares[field_name] = list(
                get_middleware_resolvers(registry.field_middlewares[field_name])
            )

    def resolve(self, next, root, info: ResolveInfo, **args):
        field_name = info.field_name
        parent_name = info.parent_type.name
        if field_name in self.field_middlewares and parent_name in ROOT_TYPES:
            middlewares = self.field_middlewares[field_name].copy()
            while middlewares:
                next = partial(middlewares.pop(), next)

        return next(root, info, **args)
