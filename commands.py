from models.user import PermissionEnum, RoleModel, PermissionModel
import click
from exts import db

def create_permission():
    for permission_name in dir(PermissionEnum):
        if permission_name.startswith("__"):
            continue
        permission = PermissionModel(name=getattr(PermissionEnum, permission_name))
        db.session.add(permission)
    db.session.commit()
    click.echo("权限添加成功！")    

def create_role():
    inspector = RoleModel(name="稽查", desc="负责审核帖子和评论是否合法合规！")
    inspector.permissions = PermissionModel.query.filter(PermissionModel.name.in_([PermissionEnum.POST, PermissionEnum.COMMENT])).all()

    
    operator = RoleModel(name="运营", desc="负责网站持续正常运行！")
    operator.permissions = PermissionModel.query.filter(PermissionModel.name.in_([PermissionEnum.POST, 
                                                                                  PermissionEnum.COMMENT,
                                                                                  PermissionEnum.BOARD,
                                                                                  PermissionEnum.FRONT_USER,
                                                                                  PermissionEnum.CMS_USER])).all()
    
    administrator = RoleModel(name="管理员", desc="负责整个网站所有工作！")
    administrator.permissions = PermissionModel.query.all()
    
    db.session.add_all([inspector, operator, administrator])
    db.session.commit()
    click.echo("角色添加成功！")        