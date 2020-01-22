"""Facebook Messenger for Python.

Copyright:
    (c) 2015 - 2018 by Taehoon Kim
    (c) 2018 - 2020 by Mads Marquart

License:
    BSD 3-Clause, see LICENSE for more details.
"""

import logging as _logging

# Set default logging handler to avoid "No handler found" warnings.
_logging.getLogger(__name__).addHandler(_logging.NullHandler())

# The order of these is somewhat significant, e.g. User has to be imported after Thread!
from . import _core, _util
from ._core import Image
from ._exception import (
    FacebookError,
    HTTPError,
    ParseError,
    ExternalError,
    GraphQLError,
    InvalidParameters,
    NotLoggedIn,
    PleaseRefresh,
)
from ._session import Session
from ._thread import ThreadLocation, ThreadABC, Thread
from ._user import User, UserData, ActiveStatus
from ._group import Group, GroupData
from ._page import Page, PageData
from ._message import EmojiSize, Mention, Message, MessageData
from ._attachment import Attachment, UnsentMessage, ShareAttachment
from ._sticker import Sticker
from ._location import LocationAttachment, LiveLocationAttachment
from ._file import FileAttachment, AudioAttachment, ImageAttachment, VideoAttachment
from ._quick_reply import (
    QuickReply,
    QuickReplyText,
    QuickReplyLocation,
    QuickReplyPhoneNumber,
    QuickReplyEmail,
)
from ._poll import Poll, PollOption
from ._plan import GuestStatus, Plan, PlanData

# Listen events
from ._event_common import Event, UnknownEvent, ThreadEvent
from ._client_payload import (
    ReactionEvent,
    UserStatusEvent,
    LiveLocationEvent,
    UnsendEvent,
    MessageReplyEvent,
)
from ._delta_class import (
    PeopleAdded,
    PersonRemoved,
    TitleSet,
    UnfetchedThreadEvent,
    MessagesDelivered,
    ThreadsRead,
    MessageEvent,
    ThreadFolder,
)
from ._delta_type import (
    ColorSet,
    EmojiSet,
    NicknameSet,
    AdminsAdded,
    AdminsRemoved,
    ApprovalModeSet,
    CallStarted,
    CallEnded,
    CallJoined,
    PollCreated,
    PollVoted,
    PlanCreated,
    PlanEnded,
    PlanEdited,
    PlanDeleted,
    PlanResponded,
)
from ._event import Typing, FriendRequest, Presence
from ._mqtt import Listener

from ._client import Client

__version__ = "1.9.6"

__all__ = ("Session", "Listener", "Client")


from . import _fix_module_metadata

_fix_module_metadata.fixup_module_metadata(globals())
del _fix_module_metadata
