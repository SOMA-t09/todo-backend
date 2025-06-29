from pydantic import BaseModel, EmailStr

# ユーザー登録用のスキーマ
class UserCreate(BaseModel):
    username: str  # ユーザー名
    email: EmailStr  # メールアドレス（形式チェック付き）
    password: str  # パスワード

    class Config:
        from_attributes = True

# ユーザーログイン用のスキーマ
class UserLogin(BaseModel):
    username: str  # ユーザー名
    password: str  # パスワード

    class Config:
        from_attributes = True