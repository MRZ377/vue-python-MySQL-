<template>
    <div class="warp">
        <div class="addchapter">
            <h2>修改章节</h2>
            <form @submit.prevent="handleSubmit()">
                <label for="">章节名称：</label>
                <input type="text" v-model="form.title" required>
                <label for="">章节内容：</label>
                <input type="file" @change="selectFile" accept=".txt,.docx,.html">
                <button type="submit">提交</button>
            </form>
            <form @submit.prevent="handleSearch()">
                <label for="">书名：</label>
                <input type="text" v-model="query.bookname">
                <label for="">作者：</label>
                <input type="text" v-model="query.author">
                <label for="">章节名称：</label>
                <input type="text" v-model="query.chaptername">
                <button type="submit">查询</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { reactive, computed, onMounted  } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore()
const query = reactive({
    bookname:'',
    author:'',
    chaptername:''
})
const form = reactive({
    bookname:query.bookname,
    author:query.author,
    old_title:query.chaptername,
    title:'',
    file:null
})
const router = useRouter()
const permissions = computed(() => store.getters.getUser?.permission)
const isLoggedIn = computed(() => store.getters.getLoginState)

function selectFile(e){
    form.file = e.target.files[0] || null
}

async function handleSearch() {
    if (permissions.value !== 'admin'){
        alert("当前帐号不是管理员账号，无权修改")
        return
    }
    if(!query.bookname || !query.author || !query.chaptername){
        alert('书名，作者或章节名称为空')
        return
    }
    try{
        const data = await store.dispatch('searchchapter', {bookname:query.bookname, author:query.author, title:query.chaptername})
        if (!data){
            alert("查询错误")
            return
        }
        Object.assign(form,data)
    }catch(e){
        alert(e?.response?.data?.message || '添加失败')
    }
}

async function handleSubmit() {
    if (permissions.value !== 'admin'){
        alert("当前帐号不是管理员账号，无权修改")
        return
    }
    if (!form.title){
        alert('书名，作者，章节名称为空')
        return
    }
    if (!form.file){
        alert('未选择章节文件')
        return
    }
    const fd = new FormData()
    fd.append('bookname', query.bookname)
    fd.append('author', query.author)
    fd.append('title', form.title)
    fd.append('old_title',query.chaptername)
    fd.append('file', form.file)
    try{
        const res = await store.dispatch('updatechapter', fd)
        alert(res.message || '修改成功')
        form.bookname = '',form.title = '',form.author = '',form.file = null
        document.querySelector('input[type="file"]').value = ''
    }catch(e){
        alert(e?.response?.data?.message || '修改失败')
    }
}

onMounted(() =>{
    store.commit('restoreUser')
    if(!isLoggedIn.value){
        alert("当前尚未登录")
        router.replace('/')
    }
})

</script>

<style scoped>
.addchapter form button{
    height: 40px;
    font-size: 24px;
    margin: 10px;
    border: none;
    background: none repeat scroll rgb(130, 196, 244);
    color: white;
}
.addchapter form input{
    height: 26px;
    margin: 10px;
}
.addchapter form label{
    font-size: 20px;
    color: rgb(92, 111, 111);
    margin: 10px;
}
.addchapter form{
    display: flex;
    flex-direction: column;
    
}
.addchapter h2{
    margin: 0;
    display: flex;
    align-items: center;
    height: 40px;
    justify-content: center;
    width: 100%;
    color: white;
    font-weight: 500;
    font-size: 26px;
    background: none repeat scroll rgb(80, 161, 162);
    border-radius: 12px 12px 0px 0px;
}
.addchapter{
    display: block;
    margin: 10px;
    border: 3px solid rgb(118, 159, 160);
    padding-bottom: 10px;
    border-radius: 15px;
}
</style>