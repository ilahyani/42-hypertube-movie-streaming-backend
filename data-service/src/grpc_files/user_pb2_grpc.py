# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from src.grpc_files import user_pb2 as user__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in user_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class loginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.loginService = channel.unary_unary(
                '/user.login/loginService',
                request_serializer=user__pb2.loginRequest.SerializeToString,
                response_deserializer=user__pb2.loginResponse.FromString,
                _registered_method=True)


class loginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def loginService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_loginServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'loginService': grpc.unary_unary_rpc_method_handler(
                    servicer.loginService,
                    request_deserializer=user__pb2.loginRequest.FromString,
                    response_serializer=user__pb2.loginResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.login', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.login', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class login(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def loginService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.login/loginService',
            user__pb2.loginRequest.SerializeToString,
            user__pb2.loginResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class signupStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.signupService = channel.unary_unary(
                '/user.signup/signupService',
                request_serializer=user__pb2.signupRequest.SerializeToString,
                response_deserializer=user__pb2.signupResponse.FromString,
                _registered_method=True)


class signupServicer(object):
    """Missing associated documentation comment in .proto file."""

    def signupService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_signupServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'signupService': grpc.unary_unary_rpc_method_handler(
                    servicer.signupService,
                    request_deserializer=user__pb2.signupRequest.FromString,
                    response_serializer=user__pb2.signupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.signup', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.signup', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class signup(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def signupService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.signup/signupService',
            user__pb2.signupRequest.SerializeToString,
            user__pb2.signupResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class addUserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addUserService = channel.unary_unary(
                '/user.addUser/addUserService',
                request_serializer=user__pb2.addUserRequest.SerializeToString,
                response_deserializer=user__pb2.addUserResponse.FromString,
                _registered_method=True)


class addUserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def addUserService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_addUserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addUserService': grpc.unary_unary_rpc_method_handler(
                    servicer.addUserService,
                    request_deserializer=user__pb2.addUserRequest.FromString,
                    response_serializer=user__pb2.addUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.addUser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.addUser', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class addUser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def addUserService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.addUser/addUserService',
            user__pb2.addUserRequest.SerializeToString,
            user__pb2.addUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class getUserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getUserService = channel.unary_unary(
                '/user.getUser/getUserService',
                request_serializer=user__pb2.getUserRequest.SerializeToString,
                response_deserializer=user__pb2.getUserResponse.FromString,
                _registered_method=True)


class getUserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getUserService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getUserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getUserService': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserService,
                    request_deserializer=user__pb2.getUserRequest.FromString,
                    response_serializer=user__pb2.getUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.getUser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.getUser', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class getUser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getUserService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.getUser/getUserService',
            user__pb2.getUserRequest.SerializeToString,
            user__pb2.getUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class searchUsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.searchUsersService = channel.unary_unary(
                '/user.searchUsers/searchUsersService',
                request_serializer=user__pb2.searchUsersRequest.SerializeToString,
                response_deserializer=user__pb2.searchUsersResponse.FromString,
                _registered_method=True)


class searchUsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def searchUsersService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_searchUsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'searchUsersService': grpc.unary_unary_rpc_method_handler(
                    servicer.searchUsersService,
                    request_deserializer=user__pb2.searchUsersRequest.FromString,
                    response_serializer=user__pb2.searchUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.searchUsers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.searchUsers', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class searchUsers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def searchUsersService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.searchUsers/searchUsersService',
            user__pb2.searchUsersRequest.SerializeToString,
            user__pb2.searchUsersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class updateUsernameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.updateUsernameService = channel.unary_unary(
                '/user.updateUsername/updateUsernameService',
                request_serializer=user__pb2.updateUsernameRequest.SerializeToString,
                response_deserializer=user__pb2.updateUsernameResponse.FromString,
                _registered_method=True)


class updateUsernameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def updateUsernameService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_updateUsernameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'updateUsernameService': grpc.unary_unary_rpc_method_handler(
                    servicer.updateUsernameService,
                    request_deserializer=user__pb2.updateUsernameRequest.FromString,
                    response_serializer=user__pb2.updateUsernameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.updateUsername', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.updateUsername', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class updateUsername(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def updateUsernameService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.updateUsername/updateUsernameService',
            user__pb2.updateUsernameRequest.SerializeToString,
            user__pb2.updateUsernameResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class updateEmailStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.updateEmailService = channel.unary_unary(
                '/user.updateEmail/updateEmailService',
                request_serializer=user__pb2.updateEmailRequest.SerializeToString,
                response_deserializer=user__pb2.updateEmailResponse.FromString,
                _registered_method=True)


class updateEmailServicer(object):
    """Missing associated documentation comment in .proto file."""

    def updateEmailService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_updateEmailServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'updateEmailService': grpc.unary_unary_rpc_method_handler(
                    servicer.updateEmailService,
                    request_deserializer=user__pb2.updateEmailRequest.FromString,
                    response_serializer=user__pb2.updateEmailResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.updateEmail', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.updateEmail', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class updateEmail(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def updateEmailService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.updateEmail/updateEmailService',
            user__pb2.updateEmailRequest.SerializeToString,
            user__pb2.updateEmailResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class updateFirstnameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.updateFirstnameService = channel.unary_unary(
                '/user.updateFirstname/updateFirstnameService',
                request_serializer=user__pb2.updateFirstnameRequest.SerializeToString,
                response_deserializer=user__pb2.updateFirstnameResponse.FromString,
                _registered_method=True)


class updateFirstnameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def updateFirstnameService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_updateFirstnameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'updateFirstnameService': grpc.unary_unary_rpc_method_handler(
                    servicer.updateFirstnameService,
                    request_deserializer=user__pb2.updateFirstnameRequest.FromString,
                    response_serializer=user__pb2.updateFirstnameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.updateFirstname', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.updateFirstname', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class updateFirstname(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def updateFirstnameService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.updateFirstname/updateFirstnameService',
            user__pb2.updateFirstnameRequest.SerializeToString,
            user__pb2.updateFirstnameResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class updateLastnameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.updateLastnameService = channel.unary_unary(
                '/user.updateLastname/updateLastnameService',
                request_serializer=user__pb2.updateLastnameRequest.SerializeToString,
                response_deserializer=user__pb2.updateLastnameResponse.FromString,
                _registered_method=True)


class updateLastnameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def updateLastnameService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_updateLastnameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'updateLastnameService': grpc.unary_unary_rpc_method_handler(
                    servicer.updateLastnameService,
                    request_deserializer=user__pb2.updateLastnameRequest.FromString,
                    response_serializer=user__pb2.updateLastnameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.updateLastname', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user.updateLastname', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class updateLastname(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def updateLastnameService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user.updateLastname/updateLastnameService',
            user__pb2.updateLastnameRequest.SerializeToString,
            user__pb2.updateLastnameResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)