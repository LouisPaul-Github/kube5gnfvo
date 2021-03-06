# Generated by Django 2.2.3 on 2019-09-27 12:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VnfPkgInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vnfdId', models.TextField(blank=True, null=True)),
                ('vnfProvider', models.TextField(blank=True, null=True)),
                ('vnfProductName', models.TextField(blank=True, null=True)),
                ('vnfSoftwareVersion', models.TextField(blank=True, null=True)),
                ('vnfdVersion', models.TextField(blank=True, null=True)),
                ('onboardingState', models.TextField(default='CREATED')),
                ('operationalState', models.TextField(default='DISABLED')),
                ('usageState', models.TextField(default='NOT_IN_USE')),
                ('userDefinedData', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VnfPkgInfoLinks',
            fields=[
                ('_links', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True,
                                                related_name='vnf_package_info_fk_link', serialize=False,
                                                to='VnfPackageManagement.VnfPkgInfo')),
                ('link_self', models.URLField()),
                ('vnfd', models.URLField()),
                ('packageContent', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='VnfPackageSoftwareImageInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('provider', models.TextField()),
                ('version', models.TextField()),
                ('containerFormat', models.TextField(default='DOCKER')),
                ('diskFormat', models.TextField(default='RAW')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('minDisk', models.TextField(blank=True, null=True)),
                ('minRam', models.TextField(blank=True, null=True)),
                ('size', models.TextField(blank=True, null=True)),
                ('userMetadata', models.TextField(blank=True, null=True)),
                ('imagePath', models.TextField(blank=True, null=True)),
                ('softwareImages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                     related_name='vnf_package_info_fk_software_image_info',
                                                     to='VnfPackageManagement.VnfPkgInfo')),
            ],
        ),
        migrations.CreateModel(
            name='VnfPackageArtifactInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artifactPath', models.TextField()),
                ('metadata', models.TextField(blank=True, null=True)),
                ('additionalArtifacts',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='vnf_package_info_fk_artifactInfo',
                                   to='VnfPackageManagement.VnfPkgInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Checksum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('algorithm', models.TextField()),
                ('hash', models.TextField()),
                ('vnf_package_artifact_info_fk_checksum',
                 models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                      related_name='vnf_package_artifact_info_fk_checksum',
                                      to='VnfPackageManagement.VnfPackageArtifactInfo')),
                ('vnf_package_info_fk_checksum',
                 models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                      related_name='vnf_package_info_fk_checksum',
                                      to='VnfPackageManagement.VnfPkgInfo')),
            ],
        ),
    ]
