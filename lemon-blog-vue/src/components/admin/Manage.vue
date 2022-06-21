<template>
<div>
    <AdminNav></AdminNav>
    <div class="articles-area">
        <el-card style="text-align: left">
            <div v-for="article in articles" :key="article.id" class="articleItem">
                <div >
                    <router-link class="article-link" :to="{path:'/blog/article',query:{id: article.id}}"><span style="font-size: 20px;"><strong>{{article.title}}</strong></span></router-link>
                    <el-divider content-position="left">{{ article.username }}</el-divider>
                    <router-link class="article-link" :to="{path:'/blog/article',query:{id: article.id}}"><p>{{article.abstract}}</p></router-link>
                </div>
                <el-divider content-position="right">{{ article.date }}</el-divider>
                <el-button type="primary" @click="onUpdate(article.id)">修改文章</el-button>
                <!-- 气泡弹出框:删除功能 -->
                <el-popover
                placement="bottom"
                width="200"
                trigger="click"
                :content="deleteMsg"
                >
                    <el-button slot="reference" @click="onDelete(article.id)">删除文章</el-button>
                </el-popover>
            </div>
            <!-- 分页器 -->
            <el-pagination
            background
            layout="total, prev, pager, next, jumper"
            @current-change="handleCurrentChange"
            :page-size="pageSize"
            :total="total"
            style="padding-left: 33%">
            </el-pagination>
        </el-card>
    </div>
</div>
</template>

<script>
  import AdminNav from '../common/AdminNav'
  export default {
    name: 'Manage',
    components: {AdminNav},
    data () {
      return {
        username: window.localStorage.getItem('user'),
        cal: new Date(),
        articles: [],
        pageSize: 4,
        total: 0,
        deleteMsg: ''
      }
    },
    mounted() {
        this.loadArticles()
    },
    methods: {
        loadArticles() {
            var _this = this

            // 获取当前用户的文章总数
            this.$axios.get('/get/' + window.localStorage.getItem('user') + '/articles')
            .then((resp) => {
                console.log(resp.data);       
                if(resp.data.code == 200) {
                    _this.total = Object.keys(resp.data['articles']).length
                } else {
                    console.log('请求文章总数出错');
                }
            }).catch((err) => {
                
            });
            
            // 获取用户第一页的文章数据
            this.$axios.get('/get/' + window.localStorage.getItem('user') + '/articles/1')
            .then((resp) => {
                console.log(resp.data);       
                if(resp.data.code == 200) {
                    // 获取文章列表
                    _this.articles = resp.data['articles']
                } else {
                    console.log('请求文章列表出错');
                }
            }).catch((err) => {
                
            });
        },
        handleCurrentChange(page) {
            var _this = this
            this.$axios.get('/get/' + window.localStorage.getItem('user') + '/articles/' + page)
            .then((resp) => {
                console.log(resp.data);       
                if(resp.data.code == 200) {
                    // 获取文章列表
                    _this.articles = resp.data['articles']
                }
            }).catch((err) => {
                
            });
        },
        onUpdate(id) {
            // 跳转到更新文章的组件 参数为文章的id
            this.$router.push({path: '/admin/article/modify', query: {id: id}})
        },
        onDelete(id) {
            // 删除文章
            var _this = this
            // this.$router.push({path: '/admin/article/delete', query: {id: id}})
            this.$axios.get('/delete/article/' + id)
            .then((resp) => {
                if(resp.data.code == 200) {
                    _this.deleteMsg = resp.data.message
                    location.reload()
                }
            }).catch((err) => {
                
            });
        }
    }
  }
</script>

<style scoped>

    .articles-area {
        width: 990px;
        height: 750px;
        margin-left: auto;
        margin-right: auto;
    }

    .article-link {
        text-decoration: none;
        color: #606266;
    }

    .article-link:hover {
        color: #409EFF;
    }

    .articleItem {
        padding: 50px;
    }

</style>