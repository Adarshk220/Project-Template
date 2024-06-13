# -*- coding: utf-8 -*-


from odoo import models, fields


class ProjectProject(models.Model):
    """Model for inheritance in project"""
    _inherit = "project.project"

    button_click = fields.Boolean(default=False)

    def action_create_project_template(self):
        """Function for the button, to create project template"""
        self.env['project.template'].create({
            'name': self.name,
            'task_name': self.label_tasks,
            'manager_id': self.user_id.id,
            'tag_ids': self.tag_ids.ids,
            'date_start': self.date_start,
            'date': self.date,
            'task_ids': self.task_ids,
        })
        self.button_click = True
        return {
            'name': 'Project Template',
            'type': 'ir.actions.act_window',
            'res_model': 'project.template',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
