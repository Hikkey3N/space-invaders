using System.Collections;
using UnityEngine;

namespace SpaceInvaders
{
    [RequireComponent(typeof(Animator))]
    public class PlayerController : EntityController
    {
        [SerializeField, Header("Key Bindings")]
        private KeyCode fireLaserKey = KeyCode.Space;
        [SerializeField]
        private KeyCode fireMissileKey = KeyCode.LeftControl;
        [SerializeField]
        private KeyCode omegaRayKey = KeyCode.RightControl;
        [SerializeField]
        private KeyCode pulseShieldKey = KeyCode.UpArrow;
        [SerializeField]
        private KeyCode moveRightKey = KeyCode.RightArrow;
        [SerializeField]
        private KeyCode moveLeftKey = KeyCode.LeftArrow;
        [SerializeField, Space]
        private float speed = 300f;
        [SerializeField, Header("Special Weapons")]
        private OmegaRayController omegaRay;
        [SerializeField]
        private PulseShieldController pulseShield;

        private Animator animator;

        public override void Spawn(Vector2 position, Vector2 direction)
        {
            base.Spawn(position, direction);
            if (animator != null)
            {
                animator.enabled = false;
            }
        }

        protected override void Awake()
        {
            base.Awake();
            animator = GetComponent<Animator>();
            gameManager.Register(this as PlayerController);
            gameManager.Register(this as IShooter);
        }

        protected override IEnumerator ExplosionCoroutine()
        {
            if (animator != null)
            {
                animator.enabled = true;
            }
            yield return base.ExplosionCoroutine();
        }

        private void Update()
        {
            if (IsExploding || omegaRay.IsFiring)
            {
                return;
            }

            if (Input.GetKeyDown(fireLaserKey))
            {
                FirePrimaryWeapon();
            }

            if (Input.GetKeyDown(fireMissileKey))
            {
                FireSecondaryWeapon();
            }

            if (Input.GetKeyDown(omegaRayKey))
            {
                FireOmegaRay();
            }

            if (Input.GetKeyDown(pulseShieldKey))
            {
                DeployPulseShield();
            }

#if DEVELOPMENT_BUILD || UNITY_EDITOR
            // Sepukku
            if (Input.GetKeyDown(KeyCode.D))
            {
                Destroy();
            }

            // Developer God mode
            if (Input.GetKeyDown(KeyCode.G))
            {
                maxHP = Health = 10000;
                FindObjectOfType<ProjectileSpawner>().maxPrimaryProjectilesActive = 10;
                FindObjectOfType<ProjectileSpawner>().maxSecondaryProjectilesActive = 10;
                omegaRay.duration = pulseShield.duration = 5f;
                omegaRay.chargeTime = pulseShield.rechargeTime = 0.5f;
            }
#endif
        }

        private void FixedUpdate()
        {
            if (IsExploding || omegaRay.IsFiring)
            {
                return;
            }

            if (Input.GetKey(moveRightKey))
            {
                Move(Vector2.right);
            }
            else if (Input.GetKey(moveLeftKey))
            {
                Move(Vector2.left);
            }
        }

        private void Move(Vector2 direction)
        {
            Vector2 target = RBPosition + speed * Time.fixedDeltaTime * direction;
            rb2D.MovePosition(target);
        }

        private void FireOmegaRay()
        {
            Vector2 offset = Vector2.up * 32;
            omegaRay.Spawn(RBPosition + offset, Vector2.up);
        }

        private void DeployPulseShield()
        {
            Vector2 offset = Vector2.up * 32;
            pulseShield.Spawn(RBPosition + offset, Vector2.up);
        }
    }
}