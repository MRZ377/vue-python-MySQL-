<template>
    <div class="wrap">
        <div class="content_block">
            <div class="top_warp">
                <div class="wap_none">
                    <a href="/">首页</a>
                    >
                    <a :href="`/book/${bookid}`">{{ bookname }}</a>
                    >
                    {{ title }}
                </div>
                <div class="btn_reader">
                    字体：
                    <button class="btn_text" @click="fontsize='large'">大</button>
                    <button class="btn_text" @click="fontsize='medium'">中</button>
                    <button class="btn_text" @click="fontsize='small'">小</button>
                    <button class="btn_text" @click="toggleEye">护眼</button>
                    <button class="btn_text" @click="toggleDark">关灯</button>
                </div>
            </div>
            <div class="content">
                <h1>{{ title }}</h1>
                <div id="chaptercontent" :class="contentClass" style="white-space: pre-line;">{{ content }}</div>
            </div>
            <div class="change">
                <router-link v-if="+chapter_no > 1" :to="`/books/${bookid}/${Number(chapter_no) - 1}`">上一章</router-link>
                <router-link :to="{name:'bookdetail', params:{bookid}}">目录</router-link>
                <router-link :to="`/books/${bookid}/${Number(chapter_no) + 1}`">下一章</router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref, watch, computed, onMounted} from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore()
const route = useRoute()
const bookid = route.params.bookid
const chapter_no = route.params.chapter_no
const content = ref('')
const title = ref('')
const bookname = ref('')
const fontsize = ref('medium')
const currentMode = ref('')

function toggleEye(){
    currentMode.value = currentMode.value === 'eye' ? '' : 'eye'
}
function toggleDark(){
    currentMode.value = currentMode.value === 'dark' ? '' : 'dark'
}
function extractBody(html){
    const match = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
    return match ? match[1].trim():html.trim();
}
const contentClass = computed(() =>['chaptercontent',`size-${fontsize.value}`])

async function load() {
    try{
        const {data} = await store.dispatch('getContent',{bookid:bookid,chapter_no:chapter_no})
        title.value = data.title
        bookname.value = data.bookname
        content.value = extractBody(data.content)
    }catch(e){
        console.error(e)
        content.value = e.response?.data?.message || '加载失败'
    }
}

onMounted(load)

watch(currentMode, val =>{
    document.body.className = val},
    {immediate:true}
)
watch(
    ()=>[route.params.bookid, route.params.chapter_no],
    ()=>load(),
    {immediate:true}
)
</script>

<style scoped>
.content h1{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0;
    padding: 10px;
    font-weight: 500;
    color: rgb(157, 83, 61);
}
#chaptercontent.size-large{font-size: 40px;}
#chaptercontent.size-medium{font-size: 26px;}
#chaptercontent.size-small{font-size: 20px;}
.change a:hover{
    color: orange;
}
.change a{
    text-decoration: none;
    font-size: 20px;
    font-weight: 600;
    color: rgb(96, 162, 237);
}
.change{
    background: none scroll repeat rgb(234, 232, 232);
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 150px;
    width: 100%;
    height: 50px;
    border: 1px dotted #aaa;
}
.btn_reader button:hover{
    color: red;
}
.btn_text{
    font-weight: 900;
    background: none scroll repeat wheat;
    border: none;
}
.btn_reader{
    color: aqua;
    display: flex;
    gap: 50px;
}
.top_warp a{
    color: aqua;
}
.wap_none{
    display: flex;
    width: 50%;
}
.top_warp{
    display: flex;
    background: none scroll space #aaa;
    width: 100%;
    height: 30px;
    justify-content: center;
    align-items: center;
}
.content_block{
    display: flex;
    border: 1px solid rgb(104, 234, 234);
    overflow: hidden;
    flex-wrap: wrap;
    flex-direction: column;
}
</style>