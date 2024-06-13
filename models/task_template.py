# -*- coding: utf-8 -*-


from odoo import fields, models


class TaskTemplate(models.Model):
    """Model for Task Template"""
    _name = "task.template"
    _description = "Task Template"

    name = fields.Char(string="Task Template")
    project_id = fields.Many2one("project.project", string="Project")
    milestone_id = fields.Many2one("project.milestone", string="Milestone")
    tag_ids = fields.Many2many("project.tags", string="Tags")
    assignee_ids = fields.Many2many("res.users", string="Assignees")
    date_end = fields.Datetime(string='Ending Date', copy=False)

    def action_create_task(self):
        """Function for the button, to create Task"""
        self.env['project.task'].create({
            'name': self.name,
            'project_id': self.project_id.id,
            'milestone_id': self.milestone_id.id,
            'user_ids': self.assignee_ids,
            'date_deadline': self.date_end,
            'tag_ids': self.tag_ids,
        })
