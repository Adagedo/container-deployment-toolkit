from typing import Optional, Union, Sequence, Tuple
from google.api_core.retry import AsyncRetry
from google.cloud import deploy_v1
from google.cloud.deploy_v1.types import *
from google.longrunning.operations_pb2 import Operation
from google.longrunning.operations_pb2 import CancelOperationRequest, DeleteOperationRequest, GetOperationRequest
from google.api_core.gapic_v1.method import DEFAULT
from google.oauth2 import service_account
from google.cloud.deploy_v1.services.cloud_deploy.pagers import *
from google.api_core.operation_async import AsyncOperation
from google.cloud.deploy_v1.types.cloud_deploy import *
"""
https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_CloudDeployAsyncClient
"""

""" for now the credentails will be loaded from a secure config file"""
credentials = service_account.Credentials.from_service_account_file("path/to/key.json")


class GoogleCloudDeploy:
    def __init__(self, credentials=None, client_options=None):
        self.client = deploy_v1.CloudDeployAsyncClient(
            credentials=credentials,
            transport="grpc_asyncio",
            client_options=client_options
        )

    async def abandon_release(
        self,
        name: str,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
    ) -> AbandonReleaseResponse:
        
        try:
            
            request = AbandonReleaseRequest(name=name)
        
            response = await self.client.abandon_release(
                request=request,
                retry=retry,
                timeout=timeout,
                metadata=metadata
            )

            return response
        except Exception as e:
            return e
    
    
    async def advance_rollout(
        self,
        name:Optional[str]=None,
        phase_id:Optional[str]=None, 
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
    )-> AdvanceRolloutResponse:
        
        try:
            
            request = AdvanceRolloutRequest(
                name=name, 
                phase_id=phase_id
            )
        
            response = await self.client.advance_rollout(
                request=request, 
                name=name, 
                phase_id=phase_id, 
                retry=retry, 
                timeout=timeout, 
                metadata=metadata
            )
            
            return response 
        
        except Exception as e:
            return e
        
        
        
    async def approve_rollout(
        self,
        name: str,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
    )-> ApproveRolloutResponse:
        
        try:
            
            request = ApproveRolloutRequest(name=name)
        
            response = await self.client.approve_rollout(
                request=request, 
                name= name, 
                retry=retry,
                timeout=timeout, 
                metadata=metadata
            )
            return response 
        
        except Exception as e:
            return e
    
    async def cancel_automation_run(
        self,
        name: str,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
    )-> CancelAutomationRunResponse:
        
        try:
            
            request = CancelAutomationRunRequest(name=name)
        
            response = await self.client.cancel_automation_run(
                request=request, 
                name=name, 
                retry=retry, 
                timeout=timeout, 
                metadata=metadata
            )
            
            return response 
        
        except Exception as e:
            return e 
        
    
    
    async def cancel_operation(
        self,
        name: str,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
    )-> str:
        
        try:
            request = CancelOperationRequest(name=name)
        
            response = await self.client.cancel_operation(
                request=request, 
                retry=retry, 
                metadata=metadata,
                timeout=timeout
            )   
        
            return f"canceling operation...{
                response if response is not None else "please wait..."
            }"
        
        except Exception as e:
            return e

    
    
    async def cancel_rollout(
        self,
        name: str,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
    )-> CancelRolloutResponse:
        
        try:
            request = CancelRolloutRequest(name=name)
            
            response = await self.client.cancel_rollout(
            request=request,
            name=name,
            retry=retry, 
            metadata=metadata,
            timeout=timeout
            )
            
            return response
        
        except Exception as ee:
            return ee 
        
        
    
    async def cluster_path(
        self,
        parent:Optional[str]=None,
        automation_id:Optional[str]=None,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        validate_only:Optional[bool]=False,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT
        
    )-> AsyncOperation:
        
        try:
            automation = Automation() 
            request = CreateAutomationRequest(
                parent=parent, 
                automation_id=automation_id, 
                automation=automation, 
                validate_only=validate_only
            )
            
            operation = await self.client.create_automation(
                request=request, 
                parent=parent, 
                automation=automation,
                automation_id=automation_id, 
                metadata=metadata, 
                timeout=timeout,
                retry=retry
            )
            
            print("waiting for operation to be completed...")
            
            response = operation.result()
            
            return response
        
        except Exception as e:
            return e
        
    
    async def create_custom_target_type(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        custom_target_type_id:Optional[str]=None, 
        validate_only:Optional[bool]=False
    )-> AsyncOperation:
        
        try:
            custom_target_type=CustomTargetType()
            request = CreateCustomTargetTypeRequest(
                parent=parent, 
                custom_target_type_id=custom_target_type_id,
                validate_only=validate_only,
                custom_target_type=custom_target_type
            )
            
            operation = await self.client.create_custom_target_type(
                request=request, 
                retry=retry,
                parent=parent,
                custom_target_type=custom_target_type, 
                custom_target_type_id=custom_target_type_id, 
                metadata=metadata, 
                timeout=timeout
            )
            print("awaiting operation to complete...")
            response = operation.result()
            
            return response
        
        except Exception as e:
            return e
        
    
    async def create_delivery_pipeline(
        
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
        delivery_pipeline_id:Optional[str]=None,

    )-> AsyncOperation:
        
        
        try:
            delivery_pipeline=DeliveryPipeline()
            request = CreateDeliveryPipelineRequest(
                parent=parent, 
                delivery_pipeline_id=delivery_pipeline_id, 
                validate_only=validate_only
            )
            
            operation = await self.client.create_delivery_pipeline(
                request=request, 
                retry=retry, 
                delivery_pipeline=delivery_pipeline, 
                delivery_pipeline_id=delivery_pipeline_id, 
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for operation to complete....")
            
            response = operation.result()
            
            return response
        
        except Exception as e:
            return e
            
            
    
    async def create_deploy_policy(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
        deploy_policy_id:Optional[str]=None, 
    )-> AsyncOperation:
        
        try:
            deploy_policy = DeployPolicy()
            request = CreateDeployPolicyRequest(
                parent=parent, 
                deploy_policy=deploy_policy, 
                deploy_policy_id=deploy_policy_id,
                validate_only=validate_only
                
            ) 
            
            operation = await self.client.create_deploy_policy(
                request=request, 
                retry=retry, 
                deploy_policy=deploy_policy, 
                deploy_policy_id=deploy_policy_id, 
                timeout=timeout, 
                metadata=metadata
            )
            
            print("waiting for operation to complete...")
            
            response = operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
            
    async def create_release(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
        release:Optional[Release]=None, 
        release_id:Optional[str]=None, 
    )-> AsyncOperation:
        
        try:
            
            request = CreateReleaseRequest(
                release=release, 
                release_id = release_id, 
                parent=parent, 
                validate_only=validate_only
            )
            
            operation = await self.client.create_release(
                retry=retry, 
                request=request, 
                parent=parent, 
                release_id=release_id, 
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for operation to complete...")
            
            response = operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
        
    async def create_rollout(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
        rollout:Optional[Rollout]=None, 
        rollout_id:Optional[str]=None, 
    )-> AsyncOperation:
        
        try:
            request = CreateRolloutRequest(
                rollout=rollout, 
                rollout_id=rollout_id, 
                parent=parent,
                validate_only=validate_only
            )
            
            operation = await self.client.create_rollout(
                request=request, 
                retry=retry, 
                parent=parent, 
                rollout=rollout, 
                rollout_id=rollout_id, 
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for operation to complete...")
            
            response = operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
        
    async def create_target(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
        target:Optional[Target]=None, 
        target_id:Optional[str]=None,
    )-> AsyncOperation:
        
        
        try:
            request = CreateTargetRequest(
                parent=parent, 
                target=target(), 
                target_id=target_id, 
                vlidate_only=validate_only
            )
            
            operation = await self.client.create_target(
                request=request, 
                retry=retry, 
                parent=parent, 
                target=target, 
                target_id=target_id, 
                metadata=metadata, 
                timeout=timeout
            )
            
            print("wating for operation to complete...")
            
            response = operation.result()
            return response 
        
        except Exception as e:
            return e
        
        
    
    async def delete_automation(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> AsyncOperation:
        
        try:
            
            request = DeleteAutomationRequest(
                name=name, 
                validate_only=validate_only
            )
            
            operation = await self.client.delete_automation(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for delete operation to complete...")
            
            response = operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
        
    async def delete_custom_target_types(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
            
    )-> AsyncOperation:
        
        try:
            
            request = DeleteCustomTargetTypeRequest(
                name=name,
                validate_only=validate_only
            )
            
            operation = await self.client.delete_custom_target_type(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for operation to complete...")
            
            
            response = operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
    
    async def delete_delivery_pipeline(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> AsyncOperation:
        
        
        try:
            
            request = DeleteDeliveryPipelineRequest(
                name=name, 
                validate_only=validate_only
            )
            
            operation = await self.client.delete_delivery_pipeline(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for operation to complete...")
            
            response = operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
        
    
    async def delete_deploy_policy(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> AsyncOperation:
        
        try:
            
            request = DeleteDeployPolicyRequest(
                name=name, 
                validate_only=validate_only
            )
            
            operation= await self.client.delete_deploy_policy(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            print("waiting for operation to complete...")
            
            
            response = operation.result()
            
            return response
        except Exception as e:
            return e
        
        
    async def delete_operation(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,
    )->None|str:
        
        
        try:
            request = DeleteOperationRequest(
                name=name
            )
            
            operation = await self.client.delete_operation(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            print("wating for operation to complete...")
            
            return f"deleting operation...{operation if operation is not None else "operation deleted."}"
        
        except Exception as e:
            return e
        
        
        
    async def delete_target(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> AsyncOperation:
        
        
        try:
            request = DeleteTargetRequest(
                name=name, 
                validate_only=validate_only,
            )
            
            operation = await self.client.delete_target(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            print("wating for operation to complete...")
            
            response = await operation.result()
            
            return response 
        
        except Exception as e:
            return e
        
        
    async def get_automation(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> Automation:
        
        
        try:
            
            request = GetAutomationRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_automation(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            return e
        
        
    async def get_automation_run(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> AutomationRun:
        
        try:
            
            request = GetAutomationRunRequest(
                name = name, 
                validate_only = validate_only
            )
            
            response = await self.client.get_automation_run(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            
            return e
        
        
    async def get_donfig(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )->Config:
        
        
        try:
            
            request = GetConfigRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_config(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        
        except Exception as e:
            return e
        
        
    async def get_custom_target_type(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> CustomTargetType:
        
        
        try:
            
            request = GetCustomTargetTypeRequest(
                name=name,
                validate_only=validate_only
            )
            
            response = await self.client.get_custom_target_type(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response
        
        except Exception as e:
            return e
        
        
    async def get_delivery_pipeline(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> DeliveryPipeline:
        
        try:
            
            request = GetDeliveryPipelineRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_delivery_pipeline(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        
        except Exception as e:
            return e
        
    
    async def get_deploy_policy(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )->DeployPolicy:
        
        try:
            
            request = GetDeployPolicyRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_deploy_policy(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            
            return e
        
        
    async def get_job_run(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> JobRun:
        
        try:
            
            request = GetJobRunRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_job_run(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            return e
        
        
    async def get_operation(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,  
    )->Operation:
        
        try:
            
            request = GetOperationRequest(
                name=name
            )
            
            response = await self.client.get_operation(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            return e
    
    
    async def get_release(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,
        validate_only:Optional[bool]=False
    )-> Release:
        
        try:
            
            request = GetReleaseRequest(
                name=name, 
                validate_only=validate_only
            )        
            
            response = await self.client.get_release(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            
            return response 
        
        except Exception as e:
            return e
        
        
    
    async def get_rollout(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,
        validate_only:Optional[bool]=False
    )->Rollout:
        
        try:
            
            request = GetRolloutRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_rollout(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            return e
        
    async def get_target(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,
        validate_only:Optional[bool]=False
    )->Target:
        try:
            
            request = GetTargetRequest(
                name=name, 
                validate_only=validate_only
            )
            
            response = await self.client.get_rollout(
                request=request, 
                retry=retry, 
                name=name,
                metadata=metadata, 
                timeout=timeout
            )
            
            return response 
        
        except Exception as e:
            return e
        
    
    async def ignore_job(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        name:Optional[str]=None,
        validate_only:Optional[bool]=False, 
        rollout:Optional[str]=None, 
        phase_id:Optional[str]=None, 
        job_id:Optional[str]=None
    )-> IgnoreJobResponse:
        
        try:
            
            request = IgnoreJobRequest(
                rollout=rollout, 
                phase_id=phase_id, 
                job_id=job_id, 
                validate_only=validate_only
            )
            
            response = await self.client.ignore_job(
                request=request, 
                retry=retry, 
                phase_id=phase_id,
                job_id=job_id, 
                metadata=metadata, 
                timeout=timeout
            )
            
            
            return response 
        except Exception as e:
            return e
        
    
    async def list_automation_run(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> ListAutomationRunsResponse|ListAutomationRunsAsyncPager:
        
        try:
            request = ListAutomationRunsRequest(
                parent=parent,
                validate_only=validate_only
            )
            
            result = self.client.list_automation_runs(
                request=request, 
                retry=retry, 
                parent=parent,
                metadata=metadata, 
                timeout=timeout
            )
            
            async for response in result:
                print(response)
            
            return result
        
        except Exception as e:
            return e
        
        
                
    async def list_automations(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )->ListAutomationRunsResponse | ListAutomationRunsAsyncPager:
        
        try:
            
            request = ListAutomationsRequest(
                parent=parent, 
                validate_only=validate_only
            )
            
            result = self.client.list_automations(
                request=request, 
                retry=retry, 
                parent=parent,
                metadata=metadata, 
                timeout=timeout
            )
            
            async for response in result:
                print(response)
            
            return result
        
        except Exception as e:
            return e
        
    
    
    async def list_custom_target_types(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    ) -> ListCustomTargetTypesAsyncPager | ListCustomTargetTypesResponse:
        
        try:
            
            request = ListCustomTargetTypesRequest(
                parent=parent, 
                validate_only=validate_only
            )
            
            
            result = self.client.list_custom_target_types(
                
                request=request, 
                retry=retry, 
                parent=parent,
                metadata=metadata, 
                timeout=timeout
            )
            
            async for response in result:
                print(response)
            return result 
        except Exception as e:
            return e
        
    
    async def list_delivery_pipelines(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )->ListDeliveryPipelinesAsyncPager | ListDeliveryPipelinesResponse:
        
        try:
            
            request = ListDeliveryPipelinesRequest(
                parent=parent, 
                validate_only=validate_only
            )

            result = self.client.list_delivery_pipelines(
                request=request, 
                retry=retry, 
                parent=parent,
                metadata=metadata, 
                timeout=timeout
            )
            
            
            async for response in result:
                print(response)
            
            return result
        
        
        except Exception as e:
            return e
        
        
        
    async def list_deploy_polcies(
        self,
        retry: Optional[AsyncRetry] = DEFAULT,
        timeout: Optional[Union[float, object]] = DEFAULT,
        metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]] = DEFAULT,
        parent:Optional[str]=None,  
        validate_only:Optional[bool]=False,
    )-> ListDeployPoliciesAsyncPager|ListDeployPoliciesResponse:
        
        
        try:
            
            request = ListDeployPoliciesRequest(
                parent=parent, 
                validate_only=validate_only
            )
            
            result = self.client.list_deploy_policies(
                request=request, 
                retry=retry, 
                parent=parent,
                metadata=metadata, 
                timeout=timeout
            )
            
            async for response in result:
                print(response)
            return result
        
        except Exception as e:
            return e
        
        
    
            
        
        
        
        
    
        
        
        
