import BooksAPI, { IBooksAPI } from './books'

export interface IAPI {
    books: IBooksAPI
}

export default {
    books: BooksAPI
} as IAPI