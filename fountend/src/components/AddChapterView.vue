<template>
    <div class="warp">
        <div class="addchapter">
            <h2>添加章节</h2>
            <form @submit.prevent="handleSubmit()">
                <label for="">书名：</label>
                <input type="text" v-model="form.bookname" required>
                <label for="">作者：</label>
                <input type="text" v-model="form.author" required>
                <label for="">章节名称：</label>
                <input type="text" v-model="form.chaptername" required>
                <label for="">章节内容：</label>
                <input type="file" @change="selectFile" accept=".txt,.docx,.html">
                <button type="submit">提交</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useStore } from 'vuex';

const store = useStore()
const form = reactive({
    bookname: '',
    author:'',
    chaptername:'',
    file:null
})

function selectFile(e){
    form.file = e.target.files[0] || null
}

async function handleSubmit() {
    if (!form.file){
        alert('未选择章节文件')
        return
    }
    const fd = new FormData()
    fd.append('bookname', form.bookname)
    fd.append('author', form.author)
    fd.append('chaptername', form.chaptername)
    fd.append('file', form.file)
    try{
        const res = await store.dispatch('addChapter', fd)
        alert(res.message || '添加成功')
        form.bookname = '',form.chaptername = '',form.author = '',form.file = null
        document.querySelector('input[type="file"]').value = ''
    }catch(e){
        alert(e?.response?.data?.message || '添加失败')
    }
}

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