"""
Classes from the 'Email' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


EMVIPManager = _Class("EMVIPManager")
EMVIP = _Class("EMVIP")
EMUserProfileProvider = _Class("EMUserProfileProvider")
EMUndoIndividualAction = _Class("EMUndoIndividualAction")
EMUbiquitouslyPersistedDictionary = _Class("EMUbiquitouslyPersistedDictionary")
EMThreadScope = _Class("EMThreadScope")
EMThreadCollectionItemID = _Class("EMThreadCollectionItemID")
EMStatusUpdateProvider = _Class("EMStatusUpdateProvider")
EMSecurityInformation = _Class("EMSecurityInformation")
EMSearchableIndexTopHitsQuery = _Class("EMSearchableIndexTopHitsQuery")
EMSearchableIndexTopHitsQueryResult = _Class("EMSearchableIndexTopHitsQueryResult")
EMSearchableIndexSchema = _Class("EMSearchableIndexSchema")
_EMCompoundQueryGenerator = _Class("_EMCompoundQueryGenerator")
_EMComparisionQueryGenerator = _Class("_EMComparisionQueryGenerator")
EMSearchableIndexQueryExpression = _Class("EMSearchableIndexQueryExpression")
EMSearchableIndexQuery = _Class("EMSearchableIndexQuery")
EMSearchableIndex = _Class("EMSearchableIndex")
_EMRemoteInterfaceDistantObject = _Class("_EMRemoteInterfaceDistantObject")
EMRemoteConnection = _Class("EMRemoteConnection")
_EMRemoteInterfaceDistantObjectReattempt = _Class(
    "_EMRemoteInterfaceDistantObjectReattempt"
)
EMRemoteConnectionRecoveryAssertion = _Class("EMRemoteConnectionRecoveryAssertion")
EMPersistenceLayoutManager = _Class("EMPersistenceLayoutManager")
EMOutgoingMessageRepository = _Class("EMOutgoingMessageRepository")
EMMessageDeliveryResult = _Class("EMMessageDeliveryResult")
EMOutgoingMessage = _Class("EMOutgoingMessage")
EMMessageInternalID = _Class("EMMessageInternalID")
EMMessageSigner = _Class("EMMessageSigner")
_EMMessageRepositoryMailboxPredictionObserver = _Class(
    "_EMMessageRepositoryMailboxPredictionObserver"
)
_EMMessageRepositoryCountingQueryObserver = _Class(
    "_EMMessageRepositoryCountingQueryObserver"
)
_EMMessageRepositoryQueryObserver = _Class("_EMMessageRepositoryQueryObserver")
EMMessageCollectionItemID = _Class("EMMessageCollectionItemID")
EMMessageListItemPredicates = _Class("EMMessageListItemPredicates")
EMMessageListItemChange = _Class("EMMessageListItemChange")
EMMessageListChangeObserverHelper = _Class("EMMessageListChangeObserverHelper")
EMMessageHeaders = _Class("EMMessageHeaders")
EMMessageChangeAction = _Class("EMMessageChangeAction")
EMUndoMessageAction = _Class("EMUndoMessageAction")
EMMessageTransferAction = _Class("EMMessageTransferAction")
EMMessageTransferAllAction = _Class("EMMessageTransferAllAction")
EMMessageFlagChangeAction = _Class("EMMessageFlagChangeAction")
EMMessageFlagChangeAllAction = _Class("EMMessageFlagChangeAllAction")
EMMessageDeleteAllAction = _Class("EMMessageDeleteAllAction")
EMMessageDeleteAction = _Class("EMMessageDeleteAction")
EMMessageConversationFlagChangeAction = _Class("EMMessageConversationFlagChangeAction")
EMMailToURLComponents = _Class("EMMailToURLComponents")
EMMailDropMetadata = _Class("EMMailDropMetadata")
EMMailboxScope = _Class("EMMailboxScope")
_EMSpecialMailboxScope = _Class("_EMSpecialMailboxScope")
EMListUnsubscribeSuggestion = _Class("EMListUnsubscribeSuggestion")
EMListUnsubscribeDetector = _Class("EMListUnsubscribeDetector")
EMListUnsubscribeCommandMessageHeaders = _Class(
    "EMListUnsubscribeCommandMessageHeaders"
)
EMListUnsubscribeCommand = _Class("EMListUnsubscribeCommand")
EMInternalFeaturePreferences = _Class("EMInternalFeaturePreferences")
EMInteractionLogger = _Class("EMInteractionLogger")
_EMUserActionState = _Class("_EMUserActionState")
EMFetchController = _Class("EMFetchController")
EMDaemonInterfaceRequest = _Class("EMDaemonInterfaceRequest")
EMDaemonInterface = _Class("EMDaemonInterface")
EMDaemonBooster = _Class("EMDaemonBooster")
EMMailboxChangeAction = _Class("EMMailboxChangeAction")
EMRenameMailboxChangeAction = _Class("EMRenameMailboxChangeAction")
EMMoveMailboxChangeAction = _Class("EMMoveMailboxChangeAction")
EMDeleteMailboxChangeAction = _Class("EMDeleteMailboxChangeAction")
EMCreateMailboxChangeAction = _Class("EMCreateMailboxChangeAction")
EMContentRequestOptions = _Class("EMContentRequestOptions")
EMContentRepresentation = _Class("EMContentRepresentation")
EMCollectionItemIDStateCapturer = _Class("EMCollectionItemIDStateCapturer")
EMClientState = _Class("EMClientState")
EMCertificateTrustInformation = _Class("EMCertificateTrustInformation")
EMCachingContactStore = _Class("EMCachingContactStore")
EMBlockedSenderManager = _Class("EMBlockedSenderManager")
EMActivityRegistry = _Class("EMActivityRegistry")
_EMActivityRegistryObserverWrapper = _Class("_EMActivityRegistryObserverWrapper")
EMActivity = _Class("EMActivity")
EMObjectID = _Class("EMObjectID")
EMThreadObjectID = _Class("EMThreadObjectID")
EMMessageObjectID = _Class("EMMessageObjectID")
EMMailboxObjectID = _Class("EMMailboxObjectID")
EMActivityObjectID = _Class("EMActivityObjectID")
EMRepository = _Class("EMRepository")
EMMessageRepository = _Class("EMMessageRepository")
EMMailboxRepository = _Class("EMMailboxRepository")
EMAccountRepository = _Class("EMAccountRepository")
EMAccountAuthentication = _Class("EMAccountAuthentication")
EMObject = _Class("EMObject")
EMRepositoryObject = _Class("EMRepositoryObject")
EMMessage = _Class("EMMessage")
EMMailbox = _Class("EMMailbox")
EMSmartMailbox = _Class("EMSmartMailbox")
EMCollection = _Class("EMCollection")
EMThread = _Class("EMThread")
EMMessageList = _Class("EMMessageList")
EMMailboxCollection = _Class("EMMailboxCollection")
EMAccount = _Class("EMAccount")
EMReceivingAccount = _Class("EMReceivingAccount")
EMDeliveryAccount = _Class("EMDeliveryAccount")
_EMAttachmentContentItem = _Class("_EMAttachmentContentItem")
EMListUnsubscribeMessageGenerator = _Class("EMListUnsubscribeMessageGenerator")
