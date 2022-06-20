<template>
    <el-menu :default-active="'/index'"
    router
    mode="horizontal"
    background-color="white"
    text-color="#222"
    active-text-color="red"
    style="min-width: 1300px">
        <el-menu-item index="/userhome">{{ user }}的主页</el-menu-item>
        <el-menu-item index="/allarticles">博客园林</el-menu-item>

        <a href="/admin" style="color: #222;float: right;padding: 20px;">后台管理</a>
        <i class="el-icon-menu" style="float:right;font-size: 45px;color: #222;padding-top: 8px"></i>
        <span style="position: absolute;padding-top: 20px;right: 48%;font-size: 20px;font-weight: bold">个人博客</span>
    </el-menu>
</template>

<script>
export default {
    name: 'NavMenu', 
     data() {

        return {
            user: window.localStorage.getItem('user')
        }
    },
    methods: {

    }
}
</script>

<style scoped>

</style>