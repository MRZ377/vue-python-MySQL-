<template>
    <div class="warp">
        <div class="addbookinfo">
            <h2>修改书籍</h2>
            <form @submit.prevent="handleSubmit()">
                <label for="">书名：</label>
                <input type="text" v-model="form.bookname">
                <label for="">作者：</label>
                <input type="text" v-model="form.author">
                <label for="">封面（图片路径的方式提供）：</label>
                <input type="text" v-model="form.bookimage">
                <label for="">类别：</label>
                <input type="text" v-model="form.category">
                <label for="">书籍简介：</label>
                <input type="text" v-model="form.bookinfo">
                <button type="submit">提交</button>
            </form>
            <form @submit.prevent="handleSearch()">
                <label for="">书名：</label>
                <input type="text" v-model="query.bookname">
                <label for="">作者：</label>
                <input type="text" v-model="query.author">
                <button type="submit">查询</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { reactive, onMounted, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useStore()
const query = reactive({
    bookname:'',
    author:''
})
const form = reactive({
    bookname: '',
    author: '',
    bookimage: '',
    category: '',
    bookinfo: ''
})
const permissions = computed(() => store.getters.getUser?.permission)
const isLoggedIn = computed(() => store.getters.getLoginState)

async function handleSubmit() {
    if(permissions.value !== 'admin'){
        alert("当前账号不是管理员账号，无权修改")
        return;
    }
    if(!form.bookname || !form.author || !form.bookinfo || !form.category){
        alert("作者，书名，类别，书籍简介不能为空")
        return
    }
    try{
        const res = await store.dispatch('updatebook', form)
        alert(res.message || '修改成功')
        Object.keys(form).forEach(k => form[k] = '')
    }catch(e){
        alert(e?.response?.data?.message || '修改失败')
    }
}

async function handleSearch() {
    if(permissions.value !== 'admin'){
        alert("当前账号不是管理员账号，无权修改")
        return;
    }
    if(!query.bookname || !query.author){
        alert("作者或书名为空")
        return
    }
    try{
        const data = await store.dispatch('searchbook', {bookname:query.bookname, author:query.author})
        if (!data){
            alert("查询错误")
            return
        }
        Object.assign(form,data)
    }catch(e){
        alert(e?.response?.data?.message || '查询失败')
    }
}

onMounted(() =>{
    store.commit('restoreUser')
    if (!isLoggedIn.value){
        alert("尚未登陆")
        router.replace('/')
    }
}
)

</script>

<style scoped>
.addbookinfo form button{
    height: 40px;
    font-size: 24px;
    margin: 10px;
    border: none;
    background: none repeat scroll rgb(130, 196, 244);
    color: white;
}
.addbookinfo form input{
    height: 26px;
    margin: 10px;
}
.addbookinfo form label{
    font-size: 20px;
    color: rgb(92, 111, 111);
    margin: 10px;
}
.addbookinfo form{
    display: flex;
    flex-direction: column;
    
}
.addbookinfo h2{
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
.addbookinfo{
    display: block;
    margin: 10px;
    border: 3px solid rgb(118, 159, 160);
    padding-bottom: 10px;
    border-radius: 15px;
}
</style>