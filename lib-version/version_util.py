import os

class VersionUtil:
    
    def get_version(self):
        return os.getenv('version', 'unknown')