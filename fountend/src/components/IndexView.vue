<template>
    <div class="wrap">
        <div class="hot">
            <div class="item" v-for="item in booklists" :key="item.bookid">
                <div class="image">
                    <a :href="`/book/${item.bookid}`" @click.prevent="handleopenDetail(item.bookid)">
                        <img :src="item.bookimage" alt="">
                    </a>
                </div>
                <dl>
                    <dt>
                        <span>{{ item.author }}</span>
                        <a :href="`/book/${item.bookid}`" @click.prevent="handleopenDetail(item.bookid)">{{ item.bookname }}</a>
                    </dt>
                    <dd>{{ item.bookinfo }}</dd>
                </dl>
            </div>
        </div>
        <div class="top">
            <h2>推荐</h2>
            <ul v-for="item in booklists" :key="item.bookid">
                <li>
                    <span class="a1">[{{ item.category }}]</span>
                    <span class="a2">
                        <a :href="`/book/${item.bookid}`" @click.prevent="handleopenDetail(item.bookid)">{{ item.bookname }}</a>
                    </span>
                </li>
            </ul>
        </div>
    </div>
    <div class="type">
        <div class="block" v-for="item in type1" :key="item.bookid">
            <h2>{{ item.category }}</h2>
            <div class="block_top" v-for="book in item.booklist.slice(0,1)" :key="book.bookid">
                <div class="image">
                    <a :href="`/book/${book.bookid}`" @click.prevent="handleopenDetail(book.bookid)">
                        <img :src="book.bookimage" alt="">
                    </a>
                    <dl>
                        <dt>
                            <a :href="`/book/${book.bookid}`" @click.prevent="handleopenDetail(book.bookid)">{{ book.bookname }}</a>
                        </dt>
                        <dd>{{ book.bookinfo }}</dd>
                    </dl>
                </div>
            </div>
            <div class="lis">
                <ul v-for="book in item.booklist" :key="book.bookid">
                    <li>
                        <span class="a1">[{{ item.category }}]</span>
                        <span class="a2">
                            <a :href="`/book/${book.bookid}`" @click.prevent="handleopenDetail(book.bookid)">{{ book.bookname }}</a>
                        </span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
        <div class="type">
        <div class="block" v-for="item in type2" :key="item.category">
            <h2>{{ item.category }}</h2>
            <div class="block_top">
                <div class="image">
                    <a :href="`/book/${item.bookid}`" @click.prevent="handleopenDetail(item.bookid)">
                        <img :src="item.bookimage" alt="">
                    </a>
                    <dl>
                        <dt>
                            <a :href="`/book/${item.bookid}`" @click.prevent="handleopenDetail(item.bookid)">{{ item.bookname }}</a>
                        </dt>
                        <dd>{{ item.bookinfo }}</dd>
                    </dl>
                </div>
            </div>
            <div class="lis">
                <ul v-for="item in categorylist" :key="item.category">
                    <li>
                        <span class="a1">[{{ item.category }}]</span>
                        <span class="a2">
                            <a :href="`/book/${item.bookid}`" @click.prevent="handleopenDetail(item.bookid)">{{ item.bookname }}</a>
                        </span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="up">
        <div class="newlist">
            <h2>最新小说</h2>
            <ul v-for="t in timelist" :key="t.bookid">
                <li>
                    <span class="a1">[{{ t.category }}]</span>
                    <span class="a2">
                        <a :href="`/book/${t.bookid}`" @click.prevent="handleopenDetail(t.bookid)">{{ t.bookname }}</a>
                    </span>
                </li>
            </ul>
        </div>
        <div class="newup">
            <h2>最新更新</h2>
            <ul v-for="value in chaptertimelist" :key="value.bookid">
                <li>
                    <span class="s1">[{{ value.category }}]</span>
                    <span class="s2">
                        <router-link :to="`/book/${value.bookid}`" @click.prevent="handleopenDetail(value.bookid)">{{ value.bookname }}</router-link>
                    </span>
                    <span class="s3">
                        <router-link :to="`/books/${value.bookid}/${value.chapterno}`">{{ value.title }}</router-link>
                    </span>
                    <span class="s4">{{ value.author }}</span>
                    <span class="s5">{{ value.createdtime }}</span>
                </li>
            </ul>
        </div>
    </div>
    <div class="zj">仅供学习使用</div>
</template>

<script setup>
import {ref, onMounted, computed} from 'vue';
import { useStore } from 'vuex';

const store = useStore()
const booklists = ref([])
const categorylist = ref([])
const timelist = ref([])
const chaptertimelist = ref([])

const type1 = computed(() => categorylist.value.slice(0,3))
const type2 = computed(() => categorylist.value.slice(3,6))

async function handleopenDetail(bookid) {
    store.dispatch('openDetail', bookid)
}

onMounted(async() =>{
    const data = await store.dispatch('getBookList')
    booklists.value = data || []
    const category = await store.dispatch('getTopBook')
    categorylist.value = category || []
    const timedata = await store.dispatch('gettime')
    timelist.value = timedata || []
    const chapterdata = await store.dispatch('getchaptertime')
    chaptertimelist.value = chapterdata || []
})

</script>

<style scoped>
.zj{
    width: 100%;
    font-weight: 100;
    text-align: center;
    padding: 0;
    font-size: 16px;
    float: left;
}
.s5{
    font-size: 18px;
    color: #AAA;
}
.s4{
    font-size: 18px;
    color: #AAA;
    width: 100px;
    text-align: right;
}
.s3{
    font-size: 18px;
    width: 170px;
}
.s3 a{
    text-decoration: none;
    color: #6699CC;
}
.s2{
    width: 170px;
    font-size: 18px;
}
.s2 a{
    text-decoration: none;
    color: #A6D3E8;
}
.s1{
    width: 60px;
    color: #AAA;
    font-size: 18px;
}
.newup{
    background: none repeat scroll 0 0 #FEF9EF;
    width: 68%;
    float: left;
    overflow: hidden;
    border: 3px solid #C3DFEA;
    flex-direction: column;
}
.newup h2{
    width: 100%;
    font-size: 22px;
    margin: 0;
    padding: 0;
    padding-left: 10px;
    background: none scroll space #b7b6b6;
    font-weight: 100;
}
.newup ul{
    list-style: none;
    padding: 0px 10px 10px;
    margin: 10px;
    border-bottom: 1px solid #AAA;    
}
.newup ul li{
    padding: 5px 0px 0px 0px;
    display: flex;
    gap: 5px;
}
.newup ul li span{
    padding: 0;
}
.newlist{
    background: none repeat scroll 0 0 #FEF9EF;
    width: 30%;
    float: right;
    overflow: hidden;
    border: 3px solid #C3DFEA;
    flex-direction: column;
}
.newlist h2{
    width: 100%;
    font-size: 22px;
    margin: 0;
    padding: 0;
    padding-left: 10px;
    background: none scroll space #b7b6b6;
    font-weight: 100;
}
.newlist ul{
    list-style: none;
    padding: 0px 10px 10px;
    margin: 5px;
    border-bottom: 1px solid #AAA;
}
.up{
    width: 980px;
    margin: 10px auto;
    padding: 0;
}
.lis{
    padding: 1px 0 0;
    margin-top: 5px;
}
.lis ul{
    list-style: none;
    padding: 0px 10px 0px;
}
.lis ul li{
    border-bottom: 1px solid #999;
}
.block_top{
    display: flex;
    margin: 10px 10px 0;

}
.block_top .image{
    display: flex;
    top: 0;
    left: 5px;
}
.block_top .image img{
    height: 120px;
    width: 100px;
}
.block_top dl{
    display: flex;
    flex-direction: column;
    padding-left: 20px;
    padding-right: 5px;
    padding-top: 0px;
    margin: 0;
}
.block_top dl dt{
    font-size: 14px;
    font-weight: 700;
    height: 25px;
    line-height: 25px;
    overflow: hidden;
}
.block_top dl dt a{
    color: #6699CC;
    text-decoration: none;
    font-size: 20px;
}
.block_top dl dd{
    height: 120px;
    line-height: 20px;
    overflow: hidden;
    padding: 7px 0px 0px 0px;
    color: #AAA;
    margin-left: 0px;
}
.type{
    border: 3px solid #A6D3E8;
    display: flex;
    width: 980px;
    margin: 20px auto;
    overflow: hidden;
}
.type .block{
    display: flex;
    width: 40%;
    flex-direction: column;
    background: none repeat scroll 0 0 #FEF9EF;
    border-right: 1px solid #88c6E5;
}
.block h2{
    width: 100%;
    font-size: 22px;
    margin: 0;
    padding: 0;
    background: none scroll space #b7b6b6;
    font-weight: 100;
}
.top{
    background: none repeat scroll 0 0 #FEF9EF;
    border:  3px solid #C3DFEA;
    padding: 0;
    float: right;
    width: 27%;
    height: 350px;
}
.top h2{
    font-weight: 500;
    font-size: 25px;
    padding: 0;
    padding-left: 10px;
    margin: 0;
    background: none 0 0 #e3e1e1;
    border-bottom: 1px solid #b7b6b6;
}
.top ul{
    list-style: none;
    padding: 0px 10px 0px;
}
.top ul li{
    border-bottom: 1px solid #999;
}
.a1{
    font-size: 18px;
    color: #AAA;
}
.a2{
    font-size: 18px;
    padding-left: 18px;
}
.a2 a{
    text-decoration: none;
    color: #6699CC;
}
.hot{
    background:none repeat scroll 0 0 #FEF9EF;
    border:3px solid #C3DFEA;
    padding:10px 0 0;
    float:left;
    overflow:hidden;
    width:695px;
    height: 341px;
}.class .hot{width:auto;}

.wrap, .nav{
    width: 980px;
    margin: 0 auto;
    zoom: 1;
    overflow: hidden;
}
</style>