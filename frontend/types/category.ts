export interface CategoryBase {
    name: string;
    description?: string;
}

// export interface CategoryCreate extends CategoryBase {
//     _type?: 'create';
// }

export interface CategoryRead extends CategoryBase {
    id: number;
    created_at: Date;
}

export interface CategoryUpdate extends CategoryBase {
    id: number;
}
