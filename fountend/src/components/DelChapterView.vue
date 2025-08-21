<template>
    <div class="warp">
        <div class="delbook">
            <h2>删除章节</h2>
            <form @submit.prevent="handleSubmit()">
                <label for="">书名：</label>
                <input type="text" v-model="form.bookname">
                <label for="">作者：</label>
                <input type="text" v-model="form.author">
                <label for="">章节名称：</label>
                <input type="text" v-model="form.title">
                <button type="submit">提交</button>
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
const form = reactive({
    bookname:'',
    author:'',
    title:''
})
const permissions = computed(() => store.getters.getUser?.permission)
const isLoggedIn = computed(() => store.getters.getLoginState)

async function handleSubmit() {
    if(permissions.value !== 'admin'){
        alert("当前账号不是管理员账号，无权添加书籍")
        return;
    }
    if(!form.bookname || !form.author || !form.title){
        alert("书名，作者或标题为空")
        return
    }
    try{
        const res = await store.dispatch('delchapter', form)
        alert(res.message || '删除成功')
        Object.keys(form).forEach(k => form[k] = '')
    }catch(e){
        alert(e?.response?.data?.message || '添加失败')
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
.delbook form button{
    height: 40px;
    font-size: 24px;
    margin: 10px;
    border: none;
    background: none repeat scroll rgb(130, 196, 244);
    color: white;
}
.delbook form input{
    height: 26px;
    margin: 10px;
}
.delbook form label{
    font-size: 20px;
    color: rgb(92, 111, 111);
    margin: 10px;
}
.delbook form{
    display: flex;
    flex-direction: column;
    
}
.delbook h2{
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
.delbook{
    display: block;
    margin: 10px;
    border: 3px solid rgb(118, 159, 160);
    padding-bottom: 10px;
    border-radius: 15px;
}
</style>