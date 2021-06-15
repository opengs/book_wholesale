<template>
  <q-table
    class="fit"
    :data="books"
    :columns="columns"
  >
    <template v-slot:top>
      <q-item>
        <div class="col-2 q-table__title">Books</div>
      </q-item>

      <q-space />

      <q-item>
        <q-btn
          label="Create book"
          @click="bookCreateDialog = true"
        />
        <q-dialog v-model="bookCreateDialog">
          <BooksCreate @created="onBookCreated"/>
        </q-dialog>
      </q-item>
    </template>

    <template v-slot:body-cell-actions="props">
      <q-tr class="q-pa-sm q-gutter-xs" :props="props">
        <q-btn round color="negative" icon="delete" size="md" @click="deleteBook(props.row)"/>
      </q-tr>
    </template>
  </q-table>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

import BooksCreate from '../components/BooksCreate.vue'

import { Book } from '../boot/api/books'

const columns = [
  {
    name: 'id',
    label: 'Id',
    field: 'id',
    align: 'left',
    sortable: true,
  },
  {
    name: 'title',
    label: 'Tile',
    field: 'title',
    align: 'left',
    sortable: true,
  },
  {
    name: 'author',
    label: 'Author',
    field: 'author',
    align: 'left',
    sortable: true,
  },
  {
    name: 'description',
    label: 'Description',
    field: 'description',
    align: 'left',
    sortable: false,
    required: false
  },
  {
    name: 'publication_date',
    label: 'Publication date',
    field: 'publication_date',
    align: 'left',
    sortable: true
  },
  {
    name: 'info',
    label: 'Info',
    field: 'info',
    align: 'left',
    required: false,
    sortable: false
  },
  {
    name: 'count_in_stock',
    label: 'Count in stock',
    field: 'count_in_stock',
    align: 'left',
    sortable: true
  },
  {
    name: 'price',
    label: 'Price',
    field: 'price',
    align: 'left',
    sortable: true
  },
  {
    name: 'discount',
    label: 'Discount',
    field: 'discount',
    align: 'left',
    required: false,
    sortable: true
  },
  {
    name: 'actions',
    label: 'Actions',
    align: 'left',
    sortable: false
  },
]

@Component({
    components: {
        BooksCreate
    }
})
export default class PageBooks extends Vue {
    books = [] as Array<Book>
    columns = columns
    bookCreateDialog = false
    
    async onBookCreated () {
        this.bookCreateDialog = false
        this.books = await this.$api.books.getAll()
    }

    async deleteBook (book: Book) {
        await this.$api.books.deleteBook(book.id)
        this.books = await this.$api.books.getAll()
    }

    async mounted () {
        this.books = await this.$api.books.getAll()
    }
};
</script>
