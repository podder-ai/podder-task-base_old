from podder_task_base.log.logger import Logger
from podder_task_base.log.log_setting import LogSetting

class TestLogger:
    TRACE_LOG_LEVEL = 5
    
    def setup_method(self, _method):
        setting = LogSetting().load()
        self.log_format = setting["task_log_format"]
        self.logger = Logger()
        
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

    def test_trace(self, capsys):
        self.logger.logger.setLevel(self.TRACE_LOG_LEVEL)
        self.logger._add_default_handler(self.log_format, self.TRACE_LOG_LEVEL)
        self.logger.trace("trace log")
        stdout, stderr = capsys.readouterr()
        assert "trace log" in stdout
        assert "TRACE" in stdout

    def test_customize_log(self, capsys):
        log_level_1 = 1
        self.logger.logger.setLevel(log_level_1)
        self.logger._add_default_handler(self.log_format, log_level_1)
        self.logger.customize_log(log_level_1, "customize log")
        stdout, stderr = capsys.readouterr()
        assert "customize log" in stdout
        assert "Level 1" in stdout
        log_level_51 = 51
        self.logger.customize_log(log_level_51, "customize log")
        stdout, stderr = capsys.readouterr()
        assert "Level 51" in stdout