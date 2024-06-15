export interface LoginResponse {
    access_token: string;
    refresh_token: string;
}

// Базовая модель категории
interface CategoryBase {
    name: string;
    description?: string; // Опциональное поле
}

// Для создания категории, наследует CategoryBase и не добавляет новых полей
interface CategoryCreate extends CategoryBase {}

// Для чтения данных категории, добавляет поля id и created_at
interface CategoryRead extends CategoryBase {
    id: number;
    created_at: Date;
}

// Для обновления категории, наследует CategoryBase и добавляет поле id
interface CategoryUpdate extends CategoryBase {
    id: number;
}
