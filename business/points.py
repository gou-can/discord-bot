# 个人积分

# 模拟积分
points_dt = {}


def get_points(member_id: int) -> int:
    return points_dt.get(member_id, 0)


def add_points(member_id: int, points: int):
    points_dt[member_id] = points_dt.get(member_id, 0) + points
