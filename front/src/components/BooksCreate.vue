<template>
  <q-card class="book-card">
    <q-card-section>
      <q-input label="Author" v-model="author" />
      <q-input label="Title" v-model="title" />
      <q-input label="Description" v-model="description" />
      <q-input label="Info" v-model="info" />
    </q-card-section>

    <q-card-section>
      <q-input label="Price" type="number" v-model="price" />
      <q-input label="Count in stock" type="number" v-model="count_in_stock" />
      <q-input label="Discount" type="number" v-model="discount" />
    </q-card-section>

    <q-card-actions>
      <q-btn label="Create book" class="fit" @click="createBook" />
    </q-card-actions>
  </q-card>
</template>

<script lang="ts">
import { Vue, Component, Emit } from 'vue-property-decorator';

@Component({
})
export default class PageIndex extends Vue {
    author = ''
    title = ''
    description? = ''
    publication_date = new Date()
    info? = ''
    price = 0
    count_in_stock = 0
    discount? = 0

    dateToYMD (date: Date) {
        var d = date.getDate()
        var m = date.getMonth() + 1
        var y = String(date.getFullYear())
        return '' + y + '-' + String(m<=9 ? '0' + String(m) : m) + '-' + String(d <= 9 ? '0' + String(d) : d);
    }

    @Emit('created')
    async createBook () {
        return await this.$api.books.createBook(
            {
                author: this.author,
                title: this.title,
                description: this.description,
                publication_date: this.dateToYMD(this.publication_date),
                info: this.info,
                price: Number(this.price),
                count_in_stock: Number(this.count_in_stock),
                discount: Number(this.discount)
            }
        )
    }
};
</script>

<style lang="sass" scoped>
.book-card
  width: 90%
  max-width: 500px
</style>

