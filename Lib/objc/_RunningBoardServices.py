"""
Classes from the 'RunningBoardServices' framework.
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


RBSTerminationAssertion = _Class("RBSTerminationAssertion")
RBSResourceViolationHandler = _Class("RBSResourceViolationHandler")
RBSProcessInfoPlistResult = _Class("RBSProcessInfoPlistResult")
RBSTerminateContext = _Class("RBSTerminateContext")
RBSProcessStateUpdate = _Class("RBSProcessStateUpdate")
RBSLaunchContext = _Class("RBSLaunchContext")
RBSMachPortTaskNameRight = _Class("RBSMachPortTaskNameRight")
RBSAuditToken = _Class("RBSAuditToken")
RBSRequest = _Class("RBSRequest")
RBSLaunchRequest = _Class("RBSLaunchRequest")
RBSTerminateRequest = _Class("RBSTerminateRequest")
RBSProcessExitEvent = _Class("RBSProcessExitEvent")
RBSProcessExitStatus = _Class("RBSProcessExitStatus")
RBSProcessExitContext = _Class("RBSProcessExitContext")
RBSXPCCodingArray = _Class("RBSXPCCodingArray")
RBSXPCServiceIdentity = _Class("RBSXPCServiceIdentity")
RBSXPCServiceDefinition = _Class("RBSXPCServiceDefinition")
RBSProcessMonitorConfiguration = _Class("RBSProcessMonitorConfiguration")
RBSProcessMonitor = _Class("RBSProcessMonitor")
RBSProcessLimitations = _Class("RBSProcessLimitations")
RBSProcessAssertionInfo = _Class("RBSProcessAssertionInfo")
RBSProcessState = _Class("RBSProcessState")
RBSProcessPredicateImpl = _Class("RBSProcessPredicateImpl")
RBSProcessIdentityPredicate = _Class("RBSProcessIdentityPredicate")
RBSProcessPredicateSuspendable = _Class("RBSProcessPredicateSuspendable")
RBSProcessPredicateLaunchServicesProcesses = _Class(
    "RBSProcessPredicateLaunchServicesProcesses"
)
RBSProcessIdentifierPredicate = _Class("RBSProcessIdentifierPredicate")
RBSProcessInstancePredicate = _Class("RBSProcessInstancePredicate")
RBSProcessPlatformPredicate = _Class("RBSProcessPlatformPredicate")
RBSCompoundPredicate = _Class("RBSCompoundPredicate")
RBSProcessIntPredicate = _Class("RBSProcessIntPredicate")
RBSProcessEUIDPredicate = _Class("RBSProcessEUIDPredicate")
RBSProcessStringPredicate = _Class("RBSProcessStringPredicate")
RBSProcessServiceNamePredicate = _Class("RBSProcessServiceNamePredicate")
RBSProcessLaunchdJobLabelPredicate = _Class("RBSProcessLaunchdJobLabelPredicate")
RBSProcessBeforeTranslocationBundlePathPredicate = _Class(
    "RBSProcessBeforeTranslocationBundlePathPredicate"
)
RBSProcessExtensionPointPredicate = _Class("RBSProcessExtensionPointPredicate")
RBSProcessBundleIdentifierPredicate = _Class("RBSProcessBundleIdentifierPredicate")
RBSProcessApplicationPredicate = _Class("RBSProcessApplicationPredicate")
RBSProcessEverythingPredicate = _Class("RBSProcessEverythingPredicate")
RBSProcessBKSLegacyPredicate = _Class("RBSProcessBKSLegacyPredicate")
RBSProcessPowerLogProcesses = _Class("RBSProcessPowerLogProcesses")
RBSProcessHandlePredicateImpl = _Class("RBSProcessHandlePredicateImpl")
RBSProcessPredicate = _Class("RBSProcessPredicate")
RBSProcessStateDescriptor = _Class("RBSProcessStateDescriptor")
RBSAssertionDescriptor = _Class("RBSAssertionDescriptor")
RBSAssertion = _Class("RBSAssertion")
RBSAttribute = _Class("RBSAttribute")
RBSRunningReasonAttribute = _Class("RBSRunningReasonAttribute")
RBSForceRoleManageAttribute = _Class("RBSForceRoleManageAttribute")
RBSTagAttribute = _Class("RBSTagAttribute")
RBSPersistentAttribute = _Class("RBSPersistentAttribute")
RBSSubordinateProcessAttribute = _Class("RBSSubordinateProcessAttribute")
RBSDurationAttribute = _Class("RBSDurationAttribute")
RBSLimitation = _Class("RBSLimitation")
RBSPreventLaunchLimitation = _Class("RBSPreventLaunchLimitation")
RBSCPUMaximumUsageLimitation = _Class("RBSCPUMaximumUsageLimitation")
RBSMimicTaskSuspensionAttribute = _Class("RBSMimicTaskSuspensionAttribute")
RBSGrant = _Class("RBSGrant")
RBSAppNapInactiveGrant = _Class("RBSAppNapInactiveGrant")
RBSAppNapPreventDiskThrottleGrant = _Class("RBSAppNapPreventDiskThrottleGrant")
RBSDebugGrant = _Class("RBSDebugGrant")
RBSGPUAccessGrant = _Class("RBSGPUAccessGrant")
RBSCPUMinimumUsageGrant = _Class("RBSCPUMinimumUsageGrant")
RBSPreventIdleSleepGrant = _Class("RBSPreventIdleSleepGrant")
RBSAppNapEnableGrant = _Class("RBSAppNapEnableGrant")
RBSAppNapPreventBackgroundSocketsGrant = _Class(
    "RBSAppNapPreventBackgroundSocketsGrant"
)
RBSEndowmentGrant = _Class("RBSEndowmentGrant")
RBSAppNapPreventLowPriorityCPUGrant = _Class("RBSAppNapPreventLowPriorityCPUGrant")
RBSDefineRelativeStartTimeGrant = _Class("RBSDefineRelativeStartTimeGrant")
RBSJetsamPriorityGrant = _Class("RBSJetsamPriorityGrant")
RBSAppNapPreventSuppressedCPUGrant = _Class("RBSAppNapPreventSuppressedCPUGrant")
RBSAppNapPreventTimerThrottleGrant = _Class("RBSAppNapPreventTimerThrottleGrant")
RBSCPUAccessGrant = _Class("RBSCPUAccessGrant")
RBSResistTerminationGrant = _Class("RBSResistTerminationGrant")
RBSSuspendableCPUGrant = _Class("RBSSuspendableCPUGrant")
RBSHereditaryGrant = _Class("RBSHereditaryGrant")
RBSDomainAttribute = _Class("RBSDomainAttribute")
RBSAcquisitionCompletionAttribute = _Class("RBSAcquisitionCompletionAttribute")
RBSLegacyAttribute = _Class("RBSLegacyAttribute")
RBSTarget = _Class("RBSTarget")
RBSInheritance = _Class("RBSInheritance")
RBSAssertionIdentifier = _Class("RBSAssertionIdentifier")
RBSProcessInstance = _Class("RBSProcessInstance")
RBSProcessIdentifier = _Class("RBSProcessIdentifier")
RBSProcessBundle = _Class("RBSProcessBundle")
RBSProcessIdentity = _Class("RBSProcessIdentity")
RBSAppProcessIdentity = _Class("RBSAppProcessIdentity")
RBSDaemonProcessIdentity = _Class("RBSDaemonProcessIdentity")
RBSXPCServiceProcessIdentity = _Class("RBSXPCServiceProcessIdentity")
RBSEmbeddedAppProcessIdentity = _Class("RBSEmbeddedAppProcessIdentity")
RBSInheritanceChangeSet = _Class("RBSInheritanceChangeSet")
RBSXPCMessageContext = _Class("RBSXPCMessageContext")
RBSXPCMessageReply = _Class("RBSXPCMessageReply")
RBSHandshakeResponse = _Class("RBSHandshakeResponse")
RBSXPCCoder = _Class("RBSXPCCoder")
RBSXPCMessage = _Class("RBSXPCMessage")
_RBSExpirationWarningClient = _Class("_RBSExpirationWarningClient")
RBSHandshakeRequest = _Class("RBSHandshakeRequest")
RBSProcessHandle = _Class("RBSProcessHandle")
RBSWorkloop = _Class("RBSWorkloop")
RBSConnection = _Class("RBSConnection")
RBSService = _Class("RBSService")
