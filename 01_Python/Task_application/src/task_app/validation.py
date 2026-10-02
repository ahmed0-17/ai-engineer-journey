class Validation:

    @staticmethod
    def validate_title(title: str) -> bool:
        return bool(title.strip())

    @staticmethod
    def validate_description(description: str) -> bool:
        return bool(description.strip())

    @staticmethod
    def validate_priority(priority: str) -> bool:
        return priority in ("High", "Medium", "Low")

    @staticmethod
    def validate_id(task_id: int) -> bool:
        return task_id > 0