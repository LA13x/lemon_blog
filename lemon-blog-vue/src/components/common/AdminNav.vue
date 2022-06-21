<template>
    <el-menu
        :default-active="'/admin'"
        class="el-menu-demo"
        router
        mode="horizontal"
    >
    <el-menu-item index="/admin/editor">文章发布</el-menu-item>
    <el-menu-item index="/admin/manage">文章管理</el-menu-item>
    <!-- <el-menu-item index="/admin/user">个人信息</el-menu-item> -->
    <span style="position: absolute;padding-top: 20px;right: 48%;font-size: 20px;font-weight: bold">后台管理</span>
    <el-menu-item index="/index" style="float: right;">博客主页</el-menu-item>
  </el-menu>
</template>


<script>
export default {
    name: "AdminNav",
    data() {
        return {};
    },
};
</script>