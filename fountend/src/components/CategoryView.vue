<template>
    <div class="wrap">
        <div class="block_item">
            <div class="item" v-for="book in booklist" :key="book.bookid">
                <div class="image">
                    <router-link :to="`/book/${book.bookid}`">
                        <img :src="book.bookimage" alt="">
                    </router-link>
                </div>
                <dl>
                    <dt>
                        <span>{{ book.author }}</span>
                        <router-link :to="`/book/${book.bookid}`">{{ book.bookname }}</router-link>
                    </dt>
                    <dd>
                    {{ book.bookinfo }}
                    </dd>
                </dl>

            </div>
        </div>
    </div>
</template>

<script setup>
import {ref, onMounted, watch} from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';

const route = useRoute()
const store = useStore()

const category = ref('')
const booklist = ref([])
async function load() {
    category.value = route.params.category
    booklist.value = await store.dispatch('getCategory', category.value)
}

onMounted(
    load
)
watch(()=>route.params.category, load)
</script>

<style>
.item dl dd{
    margin: 0;
}
.block_item .item{
    margin: 10px;
    width: calc(31% - (20px * 2 / 3));
}
.block_item{
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 10px;
    background: none repeat scroll rgb(255, 253, 208);
    border: 3px solid rgb(101, 228, 226);
}
</style>