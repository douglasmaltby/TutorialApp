import os
import subprocess
import sys


class CodeSign:
    def __init__(self):
        self.cwd = os.getcwd()
        self.buildPath = os.getenv('CONFIGURATION_BUILD_DIR')
        self.signingIdentity = os.getenv('CODE_SIGN_IDENTITY')
        self.sdk = os.getenv('SDK_NAME')
        print "---- Code Signing Identity ----"
        print self.signingIdentity

        self.codeSignFrameworks(self.buildPath, self.signingIdentity)

    def codeSignFrameworks(self, frameworkPath, certificate):
        frameworks = ["SAPCommon", "SAPFoundation", "SAPFiori", "SAPFioriFlows", "SAPOData", "SAPOfflineOData"]

        for framework in frameworks:

            if self.sdk.startswith('macosx'):
                binaryPath = frameworkPath + "/" + framework + ".framework/Versions/A"
                print "Signing binaries on path : " + binaryPath
                codesignCommand = ["codesign", "--timestamp", "--options=runtime", "--verbose=2", "--force", "--sign" , certificate, binaryPath]
                retCode = subprocess.call(codesignCommand)


CodeSign()