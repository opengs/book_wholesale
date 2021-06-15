import axios from 'axios'

export interface BookBase {
    author: string
    title: string
    description?: string
    publication_date: string
    info?: string
    price: number
    count_in_stock: number
    discount?: number
}

export interface Book extends BookBase {
    id: number
}

export interface BooksGetAllResponse {
    books: Array<Book>
}

export interface IBooksAPI {
    getAll(): Promise<Array<Book>>
    createBook(data: BookBase): Promise<Book>
    deleteBook(id: number): Promise<void>
}

export class BooksAPI implements IBooksAPI {
    async getAll(): Promise<Book[]> {
        const response = await axios.get('/api/books/all')
        return (response.data as BooksGetAllResponse).books
    }

    async createBook(data: BookBase): Promise<Book> {
        const response = await axios.post('/api/books/book', data)
        return response.data as Book
    }

    async deleteBook(id: number): Promise<void> {
        await axios.delete('/api/books/book', { data: { id } })
    }
}

export default new BooksAPI()