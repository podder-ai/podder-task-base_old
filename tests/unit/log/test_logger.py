from podder_task_base.log.logger import Logger

class TestLogger:

    def test_convert_newline_character_without_newline(self):
        message = Logger()._convert_newline_character("log message")
        assert message == "log message"

    def test_convert_newline_character_with_newline(self):
        message = Logger()._convert_newline_character("log\nmessage\n")
        assert message == "log\\nmessage\\n"
   
    def test_fatal(self, capsys):
        Logger().fatal("fatal log")
        stdout, stderr = capsys.readouterr()
        assert "fatal log" in stdout
        assert "CRITICAL" in stdout   

    def test_error(self, capsys):
        Logger().error("error log")
        stdout, stderr = capsys.readouterr()
        assert "error log" in stdout
        assert "ERROR" in stdout  

    def test_warn(self, capsys):
        Logger().warn("warn log")
        stdout, stderr = capsys.readouterr()
        assert "warn log" in stdout
        assert "WARNING" in stdout 

    def test_info(self, capsys):
        Logger().info("info log")
        stdout, stderr = capsys.readouterr()
        assert "info log" in stdout
        assert "INFO" in stdout 

    def test_debug(self, capsys):
        Logger().debug("debug log")
        stdout, stderr = capsys.readouterr()
        assert "debug log" in stdout
        assert "DEBUG" in stdout

    def test_trace(self):
        Logger().trace("trace log")
        pass

    def test_log(self, capsys):
        Logger().log("log")
        pass