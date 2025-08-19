<template>
    <div class="warp">
        <div class="blocks" v-for="value in categorylist" :key="value.category">
            <h2>{{ value.category }}排行榜</h2>
            <ul>
                <li v-for="book in value.booklist" :key="book.bookid">
                    <router-link :to="`/book/${book.bookid}`">{{ book.bookname }}</router-link>
                    /{{ book.author }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import { useStore } from 'vuex';

const store = useStore()
const categorylist = ref([])

async function loadtop() {
    const data = await store.dispatch('getTopBook')
    categorylist.value = data || []
}

onMounted(
    loadtop
)
</script>

<style>
.blocks ul li a{
    text-decoration: none;
    color: rgb(74, 66, 219);
    font-size: 16px;
}
.blocks ul li a:hover{
    color: #da5454;
}
.blocks ul li{
    display: inline-block;
    margin: 0;
    width: 25%;
    height: 30px;
    line-height: 30px;
    border-bottom: 1px double rgb(183, 180, 180);
}
.blocks ul{
    list-style: none;
    padding: 0;
    padding-bottom: 10px;
    margin: 0;
    overflow: hidden;
}
.blocks h2{
    margin: 0%;
    background: none repeat scroll rgb(225, 222, 222);
    border-bottom: 1px solid rgb(183, 180, 180);
    font-size: 24px;
    font-weight: 500;
    padding-left: 20px;
    display: flex;
    align-items: center;
    height: 40px;
}
.warp{
    width: 980px;
    margin: 0 auto;
    zoom: 1;
    overflow: hidden;
    margin-top: 10px;
}
</style>