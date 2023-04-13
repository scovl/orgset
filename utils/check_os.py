import platform


class checkOs:
    @staticmethod
    def detect_os():
        if platform.system() == "Linux":
            return "Linux"
        elif platform.system() == "Windows":
            return "Windows"
        elif platform.system() == "Darwin":
            return "MacOS"
        else:
            return "Sistema Operacional não suportado!"
