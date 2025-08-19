<template>
    <div class="wrap">
        <div class="so_list_bookcase">
            <h2>与“{{ keyword }}”相关的小说</h2>
            <div class="type_show">
                <div class="bookbox" v-for="book in booklist" :key="book">
                    <div class="box">
                        <div class="bookimg">
                            <router-link :to="`/book/${book.bookid}`">
                                <img :src="book.bookimage" alt="">
                            </router-link>
                        </div>
                        <div class="booksinfo">
                            <h4 class="bookname">
                                <router-link :to="`/book/${book.bookid}`">{{ book.bookname }}</router-link>
                            </h4>
                            <div class="author">作者：{{ book.author }}</div>
                            <div class="bookinfo">{{ book.bookinfo }}</div>
                        </div>
                    </div>
                </div>
            </div>
            <p v-if="booklist.length === 0">未找到对应书籍</p>
        </div>
    </div>
</template>

<script setup>
import {ref, onMounted, watch} from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

const route = useRoute()
const store = useStore()
const booklist = ref([])
const keyword = ref('')

async function loadSearch() {
    keyword.value = route.query.q || ''
    if(!keyword.value){ booklist.value =[]; return}
    booklist.value = await store.dispatch('getSearchBook', keyword.value)
}

onMounted(
    loadSearch
)
watch(()=> route.query.q, loadSearch)
</script>

<style>
.so_list_bookcase p{
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}
.bookinfo{
    color: #676363;
    font-size: 16px;
    width: 100%;
}
.author{
    color: #676363;
    font-size: 17px;
    padding-bottom: 5px;
    width: 100%;
}
.bookname a{
    color: #6699CC;
    text-decoration: none;
    font-size: 20px;
}
.bookname{
    font-size: 20px;
    margin: 0;
    width: 100%;
    padding-top: 10px;
    padding-bottom: 10px;
}
.booksinfo{
    display: flex;
    overflow: hidden;
    flex-direction: column;
}
.bookimg a{
    width: 120px;
    height: 140px;
}
.bookimg img{
    width: 120px;
    height: 140px;
}
.bookimg{
    padding: 0;
    margin: 0px 10px 0;
}
.box{
    margin: 10px 10px 0;
    padding: 15px 10px 10px 10px;
    background: none scroll repeat #efeab7;
    border: 1px solid rgb(170, 168, 168);
    display: flex;
}
.bookbox{
    width: calc(50% - 5px);
    box-sizing: border-box;
}
.type_show{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    width: 100%;
    padding-bottom: 10px;
}
.so_list_bookcase h2{
    box-sizing: border-box;
    margin: 0;
    width: 100%;
    background: none repeat scroll #e8e5e5;
    font-size: 24px;
    font-weight: 400;
    padding: 10px 0px 10px 20px;
    overflow: hidden;
}
.so_list_bookcase{
    border: 3px solid rgb(85, 203, 218);
}
.wrap{
    width: 980px;
    margin: 0 auto;
    zoom: 1;
    overflow: hidden;
}
</style>