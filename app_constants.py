class AppConstants:
    """
    Houses any data that could be used in
    multiple areas of the application.
    """
    @staticmethod
    def filePreface():
        """
        Preface for JSON file used for
        x-effect data storage.

        Returns:
            str: File preface for the x-effect data loading
        """
        return 'ld_'