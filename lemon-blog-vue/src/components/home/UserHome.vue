<template>
    <!-- 用户的主页：渲染出用户的文章列表，个人信息（左右分栏） -->
    <div>
        <el-container>
            <!-- 侧边栏信息 -->
            <el-aside width="400px" style="background:white;">
                <el-card style="margin-top:19px; margin-left:10px;">
                    <div class="information">
                        <div class="block">
                            <el-avatar :size="50" :src="imgURL"></el-avatar>
                        </div>
                        <p style="font-family: 'Hiragino Sans GB'">{{ username }}</p>
                        <el-popconfirm
                        title="确定退出登陆吗？"
                        @confirm="userLogout"
                        >
                        <el-button slot="reference" class="logout">退出登录</el-button>
                        </el-popconfirm>
                    </div>
                    <div class="cal">
                        <el-calendar v-model="cal"></el-calendar>
                    </div>
                </el-card>
            </el-aside>

            <!-- 主页信息 -->
            <el-main>
                
                <div class="articles-area">
                <el-card style="text-align: left">
                    <div v-for="article in articles" :key="article.id" class="articleItem">
                        <div >
                            <router-link class="article-link" :to="{path:'blog/article',query:{id: article.id}}"><span style="font-size: 20px;"><strong>{{article.title}}</strong></span></router-link>
                            <el-divider content-position="right">{{article.date}}</el-divider>
                            <router-link class="article-link" :to="{path:'blog/article',query:{id: article.id}}"><p>{{article.abstract}}</p></router-link>
                        </div>
                        <el-divider></el-divider>
                    </div>
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
            
            </el-main>
        </el-container>
    </div>
</template>

<script>
  export default {
    data () {
      return {
        imgURL: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        username: window.localStorage.getItem('user'),
        cal: new Date(),
        articles: [],
        pageSize: 4,
        total: 0
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
        userLogout() {
            window.localStorage.removeItem('user')
            location.reload()
        }
    }
  }
</script>

<style scoped>
    .information {
        padding: 40px;
    }

    .information p {
        margin-top: 20px;
    }

    .cal {
        margin-top: 40px;
    }

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
        padding: 25px;
    }

    .logout {
        margin-top: 40px;
    }

</style>