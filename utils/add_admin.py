from config import update_env_file


def add_admin(user_id: int) -> str:
    global admins
    from create_bot import admins

    if user_id in admins:
        return "⚠️ Этот пользователь уже админ."

    admins.append(user_id)

    new_admins_str = ",".join(map(str, admins))
    update_env_file("ADMINS", new_admins_str)

    return "Админ добавлен"
