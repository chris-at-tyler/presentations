"""Toy inventory module — exists so the demo has something real to stage and commit."""


def restock_threshold(daily_sales: float, lead_time_days: int, safety_factor: float = 1.5) -> int:
    """Units at which a reorder should trigger."""
    return int(daily_sales * lead_time_days * safety_factor)


def needs_restock(current_units: int, daily_sales: float, lead_time_days: int) -> bool:
    return current_units <= restock_threshold(daily_sales, lead_time_days)
