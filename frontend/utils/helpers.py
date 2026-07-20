def format_score(score):
    if score is None:
        return "—"
    return f"{score}/100"


def status_color(status):
    colors = {
        "completed": "#10B981",
        "running": "#3B82F6",
        "failed": "#EF4444",
        "pending": "#F59E0B",
    }
    return colors.get(status, "#6B7280")


def truncate(text, length=80):
    if not text:
        return ""
    if len(text) <= length:
        return text
    return text[:length] + "..."