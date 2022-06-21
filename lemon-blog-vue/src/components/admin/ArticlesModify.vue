<template>
    <div class="markdown">
        <AdminNav></AdminNav>
    <el-row style="margin: 18px 0px 0px 18px ">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>文章修改</el-breadcrumb-item>
      </el-breadcrumb>
    </el-row>
    <el-row>
      <el-input
        v-model="article.title"
        style="margin: 10px 0px;font-size: 18px;"
        placeholder="请输入标题"></el-input>
    </el-row>
    <el-row style="height: calc(100vh - 140px);">
      <mavon-editor
        v-model="article.md"
        style="height: 100%;"
        ref=md
        @save="updateArticles"
        fontSize="16px">
        <button type="button" class="op-icon el-icon-document" :title="'摘要'" slot="left-toolbar-after"
                @click="dialogVisible = true"></button>
      </mavon-editor>
      <el-dialog
        :visible.sync="dialogVisible"
        width="30%">
        <el-divider content-position="left">摘要</el-divider>
        <el-input
          type="textarea"
          v-model="article.abstract"
          rows="6"
          maxlength="255"
          show-word-limit></el-input>
          
        
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
    </div>
</template>

<script>
    import AdminNav from '../common/AdminNav'
    export default {
        name: "ArticlesModify",
        components: {AdminNav},
        data() {
            return {
                value: '',
                article: {},
                dialogVisible: false,
            }
        },
    
        mounted() {
            this.loadArticle()
        },
        methods: {
            loadArticle() {
                // 加载文章到editor里面
                var _this = this
                this.$axios.get('/article/' + this.$route.query.id)
                .then((resp) => {  
                    if(resp.data.code == 200) {
                    // 获取文章内容
                    _this.article = resp.data.article
                    console.log(_this.article);
                } else {
                    console.log('请求文章信息出错');
                }
                }).catch((err) => {
                    
                });
            }, 
            updateArticles (value, render) {
            // value 是 md，render 是 html
            console.log(value, render);
            this.$confirm('是否保存并修改?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
            }).then(() => {
                this.$axios
                .post('/update/article', {
                    // 修改文章
                    id: this.article.id,
                    // id: 1,
                    articleTitle: this.article.title,
                    articleContentMd: value,
                    articleContentHtml: render,
                    articleAbstract: this.article.abstract,
                    username: window.localStorage.getItem('user')
                }).then(resp => {
                if (resp && resp.data.code == 200) {
                    this.$message({
                        type: 'info',
                        message: '已修改成功'
                    }),
                    // console.log(resp.date);
                    this.$router.push({path: '/admin/manage'})
                } else {
                    console.log(resp.data);
                }
                })
            }
            ).catch(() => {
            this.$message({
                type: 'info',
                message: '已取消发布'
            })
            })
        },
    }
}

</script>

