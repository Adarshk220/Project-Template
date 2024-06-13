# -*- coding: utf-8 -*-


from odoo import models, fields


class ProjectTask(models.Model):
    """Model for inheritance in Task"""
    _inherit = "project.task"

    project_template_id = fields.Many2one("project.template")
    button_click = fields.Boolean(default=False)

    def action_create_task_template(self):
        """Function for the button, to create task template"""
        self.env['task.template'].create({
            'name': self.name,
            'project_id': self.project_id.id,
            'milestone_id': self.milestone_id.id,
            'assignee_ids': self.user_ids,
            'date_end': self.date_deadline,
            'tag_ids': self.tag_ids,
        })
        self.button_click = True
        return {
            'name': 'Task Template',
            'type': 'ir.actions.act_window',
            'res_model': 'task.template',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
