from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"


class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o método log")

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"success: {msg}")


class LogFileMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")
        msg_formatada = f"{msg}({self.__class__.__name__})"
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write("\n\r")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


if __name__ == "__main__":
    logs = LogFileMixin()
    logs.log_error("qualquer coisa")
    logs.log_success("show")
    print(LOG_FILE)
