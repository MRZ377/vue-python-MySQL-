<template>
    <div class="book">
        <div class="path wap_none">
            <a href="/">首页</a>>{{ info?.category }}>{{ info?.bookname }}
            <span class="oninfo">
                <a href="#comment" rel="nofollow" style="color: red;">直达底部</a>
            </span>
        </div>
        <div class="info">
            <div class="cover">
                <img :src="info?.bookimage" alt="">
            </div>
            <h1>{{ info?.bookname }}</h1>
            <div class="small">
                <span>作者：{{ info?.author }}</span>
                <span>状态：{{ info?.state }}</span>
                <span>更新：{{ info?.updatetime }}</span>
                <span>最新：<router-link :to="{name:'content', params:{bookid:info.bookid, chapter_no:latest.chapter_no}}">{{ latest.title }}</router-link></span>
            </div>
            <div class="readlink">
                <a href="">加入书架</a>
                <router-link :to="{name:'content', params:{bookid:info.bookid, chapter_no:list[0].chapter_no}}" class="rl">开始阅读</router-link>
            </div>
            <div class="intro">
                <dl>
                    <dt>内容简介：</dt>
                    <dd>{{ info?.bookinfo }}</dd>
                </dl>
            </div>
        </div>
    </div>
    <div class="listmain">
        <dl>
            <dt>章节列表</dt>
            <dd v-for="i in list" :key="i.chapter_no">
                <router-link :to="{name:'content', params:{bookid:info.bookid, chapter_no:i.chapter_no}}">{{ i.title }}</router-link>
            </dd>
        </dl>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import {ref, onMounted, watch} from 'vue';
import { useStore } from 'vuex';

const store = useStore()
const route = useRoute()
const info = ref({
    author:'',
    bookid:0,
    bookimage:'',
    bookname:'',
    category:'',
    createtime:'',
    bookinfo:'',
    state:'',
    updatetime:''
})
const list = ref([
    {chapter_no:0, title:''}
])
const latest = ref({
    chapter_no:0,
    title:''
})
async function loadBook() {
    const bookid = route.params.bookid
    if(history.state?.info){
        info.value = history.state.info
        list.value = history.state.list || []
        latest.value = history.state.latest
    }else{
        try{
        const {info:book, chapterlist, latest:latests} = await store.dispatch('getDetail', bookid)
        info.value = book
        list.value = chapterlist
        latest.value = latests
        }catch(e){
            console.error(e)
        }
    }
}
onMounted(()=>loadBook())
watch(
    ()=>route.fullPath,
    ()=>loadBook(),
    {immediate:false}
)
</script>

<style>
.listmain dd a{
    text-decoration: none;
    color: #06b7fd;
    font-size: 20px;
    font-weight: 300;
    line-height: 40px;
}
.listmain dd{
    margin: 0;
    display: inline-block;
    width: 33.3%;
    box-sizing: border-box;
    padding: 0px 10px;
    vertical-align: top;
    height: 40px;
    border-bottom: 2px dotted #88C6E5;
}
.listmain dt{
    width: 100%;
    height: 45px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: none scroll repeat rgb(213, 211, 211);
    font-size: 18px;
    box-sizing: border-box;
    border-bottom: 1px solid #E1ECED;
}
.listmain dl{
    margin: 0%;
    padding: 0%;
    display: block;
}
.intro dd{
    margin: 0;
}
.intro dl{
    display: flex;
    margin-top: 0;
    font-size: 18px;
    color: gray;
}
.intro{
    grid-column: 2/3;
    grid-row: 4/4;
}
.readlink .rl{
    background: none scroll space orange;
    margin-left: 50px;
}
.readlink a{
    background: none scroll space rgb(73, 150, 209);
    text-decoration: none;
    color: #ffff;
    font-size: 16px;
    font-weight: 600;
    width: 45%;
    height: 36px;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
}
.readlink{
    grid-column: 2/3;
    grid-row: 3/4;
    display: flex;
    padding: 0px 10px 10px;
}
.small span a{
    text-decoration: none;
    color: rgb(229, 64, 64);
}
.small span{
    width: 50%;
    height: 26px;
    color: rgb(102, 104, 105);
    font-size: 18px;
}
.small{
    grid-row: 2/3;
    grid-column: 2/3;
    display: flex;
    flex-wrap: wrap;
    border-bottom: 1px solid #ccc;
}
.info h1{
    grid-column: 2/3;
    grid-row: 1/2;
    margin: 0;
    width: 100%;
    height: 40px;
    font-size: 30px;
    font-weight: 500;
    color: rgb(102, 104, 105);
}
.cover img{
    height: 180px;
    width: 140px;
    border: 1px solid #ccc;
    padding: 1px;
}
.cover{
    margin: 0px 10px;
    width: 165px;
    height: 195px;
    background: none scroll repeat #ccc;
    justify-content: center;
    align-items: center;
    grid-column: 1/2;
    grid-row: 1/-1;
    display: flex;
}
.info{
    margin: 10px 0px 0px;
    overflow: hidden;
    display: grid;
    grid-template-columns: 20% 1fr;
    grid-template-rows: auto auto auto auto;
    gap: 10px;
}
.oninfo{
    font-size: 20px;
    float: right;
}
.wap_none a{
    text-decoration: none;
    color: #88C6E5;
}
.wap_none{
    display: block;
}
.book,.listmain{
    margin: 20px auto;
    width: 980px;
    border: 3px solid #C3DFEA;
    background: none repeat scroll #FEF9EF;
}
.path{
    width:auto;
    margin: 0 auto;
    height:40px;
    line-height:40px;
    overflow:hidden;
    background:#E1ECED;
    border-bottom:1px solid #88C6E5;
    padding:0 10px;
}
</style>